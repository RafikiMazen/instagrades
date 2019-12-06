from django.urls import path
from .views import homeViewFun,HomePageView,LogInPageView

urlpatterns = [
    #path('', homeViewFun, name='home'),
   path('', HomePageView.as_view(), name='home'),
   path('',LogInPageView.as_view, name='logged out')

]