from django.urls import path

from SuiteApi import views

urlpatterns = [

    path('login', views.LoginView.as_view()),
    path('logout', views.Logout.as_view()),

]
