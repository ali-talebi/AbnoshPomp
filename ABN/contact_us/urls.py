from django.urls import path 
from .views import Conatc_Us_View 
app_name = "contact_us" 
urlpatterns = [
    path("Conatc_Us_View/" , Conatc_Us_View , name="Conatc_Us_View" ) , 
    
]