from django.urls import path 
from .views import Show_Blog  , Show_detail  
app_name = "BLOG"

urlpatterns = [
    path('' ,Show_Blog , name="Show_Blog" ) , 
    path("Show_detail/<int:id>/" , Show_detail , name="Show_detail" ) , 
]
