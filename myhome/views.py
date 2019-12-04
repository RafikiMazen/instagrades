from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import request,response
import requests
def home(request):
    registration = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course_Registration')
    course= requests.get('http://5de664d29c4220001405b561.mockapi.io/Course')
    grade = requests.get('http://5de664d29c4220001405b561.mockapi.io/Grade')
    registrationData = registration.json()
    courseData = course.json()
    gradeData=grade.json()
    template_name = 'home.html'
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'