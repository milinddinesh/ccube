from django.shortcuts import redirect, render
from django.http import HttpResponse
from user_auth.models import User_info
from django.http import JsonResponse
import os
from dotenv import load_dotenv
load_dotenv()

def test(request): #test end point. 
    return HttpResponse("working")

def validate(task_id,flag):
    task_id = int(task_id)
    boo = False
    if task_id == 1:
        if flag == "correct_flag_here": #replace this with correct flag
            boo = True
        else : boo = False
    elif task_id == 2:
        print("inside2")
        if flag == "correct_flag":
            boo = True
        else : boo = False
    elif task_id == 3:
        if flag == "correct_flag":
            boo = True
        else : boo = False
    elif task_id == 4:
        if flag == "correct_flag":
            boo = True
        else : boo = False
    elif task_id == 5:
        if flag == "correct_flag":
            boo = True
        else : boo = False
    elif task_id == "6":
        if flag == "correct_flag":
            boo = True
        else : boo = False
    return boo
    

def submit(request):
    if request.method =="POST":
        task_id = request.POST.get("task")
        flag = request.POST.get("flag")
        user_email = request.COOKIES.get("user_email")
        if user_email :
            try:
                user = User_info.objects.get(email=user_email)
            except User_info.DoesNotExist :
                return HttpResponse("User not found")
            else :
                if task_id == "1":
                    if validate(task_id,flag):
                        user.task1 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task1 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
                elif task_id == "2":
                    if validate(task_id,flag):
                        print("returned true")
                        user.task2 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task2 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
                elif task_id == "3":
                    if validate(task_id,flag):
                        user.task3 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task3 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
                elif task_id == "4":
                    if validate(task_id,flag):
                        user.task4 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task4 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
                elif task_id == "5":
                    if validate(task_id,flag):
                        user.task5 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task5 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
                elif task_id == "6":
                    if validate(task_id,flag):
                        user.task6 = 5
                        user.save()
                        return HttpResponse("That's Correct!")
                    else :
                        user.task6 += 1
                        user.save()
                        return HttpResponse("Wrong Answer!")
        else:
            return HttpResponse("Submission time over")
    else:
        return HttpResponse("Invalid request method")

def getSubmissions(request):
    if request.method =="GET":
        user_email = request.COOKIES.get("user_email")
        if user_email :
            try:
                user = User_info.objects.get(email=user_email)
            except User_info.DoesNotExist :
                return HttpResponse("User does not exist")
            else :
                task_submissions={
                    'task1' : user.task1,
                    'task2' : user.task2,
                    'task3' : user.task3,
                    'task4' : user.task4,
                    'task5' : user.task5
                }
                return JsonResponse(task_submissions)
        else : return HttpResponse("Your session is over")
    else : return HttpResponse("Invalid request method")

def play(request):
    return redirect("https://vighneshhm.github.io/Crashing-Into-You-CTF/")