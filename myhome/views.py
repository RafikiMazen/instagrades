from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404
import json

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import request,response
from django.contrib.sessions.models import Session
from .models import Profile
import requests
def homeViewFun(request):
    registrationData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course_Registration')
    courseData= requests.get('http://5de664d29c4220001405b561.mockapi.io/Course')
    gradeData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Grade')
    # registrations = json.load(registrationData.text)
    # courses = json.loads(courseData.text)
    # grades=json.loads(gradeData.text)
    registrations = registrationData.json()
    courses = courseData.json()
    grades = gradeData.json()
    current_user_id=request.user.profile.id
    course_name_list = []
    course_id_list = []
    registration_id_list = []
    peer_registration_id_list = []
    user_quiz_grades_list = []
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
    return render_to_response('../templates/view.html', {'course_name_list': course_name_list, 'user_quiz_grades_list': user_quiz_grades_list})
# Create your views here.

class LogInPageView(TemplateView):
    template_name = 'home.html'

class HomePageView(TemplateView):
  template_name = 'viewrourou.html'


  #@login_required
  def get_context_data(self, **kwargs):
      if(hasattr(self.request.user,'profile')):
          context = super(HomePageView, self).get_context_data(**kwargs)
          registrationData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course_Registration')
          courseData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course')
          gradeData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Grade')
          # registrations = json.load(registrationData.text)
          # courses = json.loads(courseData.text)
          # grades=json.loads(gradeData.text)
          registrations = registrationData.json()
          courses = courseData.json()
          grades = gradeData.json()
        #  current_user_id = request.user.profile.id
          course_name_list = []
          course_id_list = []
          registration_id_list = []
          peer_registration_id_list = []
          user_quiz_grades_list = []
          current_user_id = self.request.user.profile.id
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




          context['course_name_list'] = course_name_list
          context['user_quiz_grades_list']=user_quiz_grades_list
          return context
      else:
          context = super(HomePageView, self).get_context_data(**kwargs)
          return context



  # def get(self, request, *args, **kwargs):
  #     registrationData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course_Registration')
  #     courseData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Course')
  #     gradeData = requests.get('http://5de664d29c4220001405b561.mockapi.io/Grade')
  #     # registrations = json.load(registrationData.text)
  #     # courses = json.loads(courseData.text)
  #     # grades=json.loads(gradeData.text)
  #     registrations = registrationData.json()
  #     courses = courseData.json()
  #     grades = gradeData.json()
  #     current_user_id = request.user.profile.id
  #     course_name_list = []
  #     course_id_list = []
  #     registration_id_list = []
  #     peer_registration_id_list = []
  #     user_quiz_grades_list = []
  #     current_user_id = request.user.profile.id
  #     # user courses
  #     for registration in registrations:
  #         if registration["StudentId"] == current_user_id:
  #             course_id_list.append(registration["CourseId"])
  #             registration_id_list.append(registration["id"])
  #
  #     # user grades
  #     for grade in grades:
  #         this_quiz_grade = []
  #         if grade["Course_RegistrationId"] in registration_id_list:
  #
  #             course_id = -1
  #             for registration in registrations:
  #                 if registration["id"] == grade["Course_RegistrationId"]:
  #                     course_id = registration["CourseId"]
  #             for course in courses:
  #                 if course["id"] == course_id:
  #                     this_quiz_grade.append(course["id"])
  #                     this_quiz_grade.append(course["Course_name"])
  #             this_quiz_grade.append(grade["quiz_no"])
  #             this_quiz_grade.append(grade["grade"])
  #             user_quiz_grades_list.append(this_quiz_grade)
  #
  #     for course in courses:
  #         if course["id"] in course_id_list:
  #             course_name_list.append(course["Course_name"])
  #
  #     for quiz in user_quiz_grades_list:
  #         result = 0
  #         number = 0
  #         for registration in registrations:
  #             if quiz[0] == registration["CourseId"]:
  #                 for grade in grades:
  #                     if grade["Course_RegistrationId"] == registration["id"] and quiz[2] == grade["quiz_no"]:
  #                         result = result + grade["grade"]
  #                         number = number + 1
  #
  #         quiz.append(result / number)
  #
  #     # for registration in registrations:
  #     #
  #     #
  #     #
  #     #
  #
  #    # template_name = 'home.html'
  #     return render_to_response('../templates/viewrourou.html',
  #                               {'course_name_list': course_name_list, 'user_quiz_grades_list': user_quiz_grades_list})

