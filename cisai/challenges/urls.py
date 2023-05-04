from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path('', views.challenges, name='challenges'),
    # path('register/',views.register, name='register')
    path('submit/',views.submit,name='submit'),
    path('getSubmissions/',views.getSubmissions,name="getSubmissions"),
    # path('challenges/',views.challenges,name='challenges')
    path('download/',views.download,name="download"),
    path('zipDownload/',views.zipDownload,name="zipDownload"),
]