from django.shortcuts import render
import json
from django.views.generic import TemplateView
from django.http import request,response
from .models import Profile
import requests
def home(request):
    registrationData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course_Registration')
    courseData= requests.get('http://5de664d29c4220001405b561.mockapi.io/Course')
    gradeData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Grade')
    registrations = json.load(registrationData.text)
    courses = json.loads(courseData.text)
    grades=json.loads(gradeData.text)
    current_user_id=request.user.profile.id
    course_name_list = []
    course_id_list = []
    registration_id_list = []
    peer_registration_id_list = []
    user_quiz_grades_list = []
    courses = courseData
    grades = gradeData
    current_user_id = request.user.profile.id
    # user courses
    for registration in registrations:
        if registration["StudentId"] == current_user_id:
            course_id_list.append(registration["CourseId"])
            registration_id_list.append(registration["id"])

    # user grades
    for grade in grades:
        this_quiz_grade = []
        if grade["Course_RegistrationId"] in registration_id_list:

            course_id = -1
            for registration in registrations:
                if registration["id"] == grade["Course_RegistrationId"]:
                    course_id = registration["CourseId"]
            for course in courses:
                if course["id"] == course_id:
                    this_quiz_grade.append(course["id"])
                    this_quiz_grade.append(course["Course_name"])
            this_quiz_grade.append(grade["quiz_no"])
            this_quiz_grade.append(grade["grade"])
            user_quiz_grades_list.append(this_quiz_grade)

    for course in courses:
        if course["id"] in course_id_list:
            course_name_list.append(course["Course_name"])

    for quiz in user_quiz_grades_list:
        result = 0
        number = 0
        for registration in registrations:
            if quiz[0] == registration["CourseId"]:
                for grade in grades:
                    if grade["Course_RegistrationId"] == registration["id"] and quiz[2] == grade["quiz_no"]:
                        result = result + grade["grade"]
                        number = number + 1

        quiz.append(result / number)

    # for registration in registrations:
    #
    #
    #
    #

    template_name = 'home.html'
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'