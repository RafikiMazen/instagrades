from django.db import models, connection
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return str(self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





# class Course(models.Model):
#     course_code = models.CharField(max_length=200, default="default course code")
#
#     def __str__(self):
#         return self.course_code
#     # pub_date = models.DateTimeField('date published')
#
#
# class Quiz(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
#     quiz_no = models.IntegerField(default=-1)
#     quiz_name = models.CharField(max_length=200, default="default quiz name")
#     quiz_max_grade = models.IntegerField(default=10)
#
#     def __str__(self):
#         return self.quiz_name
#
#
# class Grade(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='grades')
#     grade = models.IntegerField(default=None)
#     student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
#     grade_name = models.CharField(max_length=200, default="default grade name")
#
#
#     def __str__(self):
#         return self.grade_name

