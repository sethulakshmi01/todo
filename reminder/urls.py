from django.urls import path 
from reminder.views import SignUpView,SignInView,IndexView,TodoCreateView



urlpatterns=[
    
    path("signup/",SignUpView.as_view(),name="signup"),
    path("signin/",SignInView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="index"),
    path("add/",TodoCreateView.as_view(),name="add-todo"),


]