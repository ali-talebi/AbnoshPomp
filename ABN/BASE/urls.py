from django.urls import path 

from .views import FAQ_View , Register ,  Home , about_us , search , login_user , logout_user 
 
app_name = "BASE_app"
urlpatterns = [
    path("" , Home , name="Home" ) , 
    path("about_us/" , about_us , name="about_us" ) , 
    path("search/" , search , name = "search" ) , 
    path("login_user/" , login_user , name="login_user" ) , 
    path("logout_user/" , logout_user , name="logout_user" ) , 
    path("Register/" , Register , name="Register") , 
    path("FAQ_View/" , FAQ_View , name="FAQ_View" ) 

]