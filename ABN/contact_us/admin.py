from django.contrib import admin
from .models import Send_Message , Information_Company 
# Register your models here.

@admin.register(Information_Company)
class Information_Company_Admin(admin.ModelAdmin) :
    list_display = ("address" , "tel1" , "tel2" , "email" )  


@admin.register(Send_Message)
class Send_Message_Admin(admin.ModelAdmin) :
    list_display = ("full_name" , "phone" , "email" , "subject" , "text" , "created" , "status" )

    search_fields = ["full_name" , "subject"  , "text" , "email" ] 