from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_info
from django.db import IntegrityError
from datetime import timedelta
from django.conf import settings
import os
from dotenv import load_dotenv
load_dotenv()

def index(request):
    return render(request,'user_auth/index.html')

def register(request):
    if request.method == "POST" :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        user = User_info(first_name=first_name,last_name=last_name,email=email,phone=phone)
        try:
            user.save()
        except IntegrityError:
            return HttpResponse("Oops look like you have already finished your chances.")

        else : 
            # challenge_page = os.getenv('CHALLENGE_PAGE')
            # response = render(request, challenge_page) #change newpage to end point of challenge page.
            response = render(request, 'challenges/task.html') 
            expires = timedelta(minutes=10)
            response.set_cookie('user_email', email, max_age=expires.total_seconds())
            return response 
    else : return render(request,'user_auth/index.html')

