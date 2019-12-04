from django.urls import path
from .views import home, HomePageView

urlpatterns = [
    path('home', home, name='home'),
    path('', HomePageView.as_view(), name='home'),
]