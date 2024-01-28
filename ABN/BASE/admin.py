from django.contrib import admin
from .models import Teams_Member  , ABOUT_US , SLIDE_POSTER  , FAQ 
from django.utils.html import format_html 
# Register your models here.


@admin.register(FAQ)
class FAQ_Admin(admin.ModelAdmin) : 
    list_display = ("q1" , "a1"  )






@admin.register(SLIDE_POSTER)
class SLIDE_POSTER_Admin(admin.ModelAdmin) : 
    list_display = ("name" , "show_img" )


    def show_img(self , obj ) : 
        return format_html('<img width=50px height = 50px src="{}">'.format(obj.picture.url))

    show_img.short_description = "تصویر"



@admin.register(Teams_Member)
class Teams_Member_Admin(admin.ModelAdmin) : 
    list_display = ("full_name" , "show_img" , "text" )

    def show_img(self , obj ) : 
        return format_html('<img width=50px height = 50px src="{}">'.format(obj.picture.url))



@admin.register(ABOUT_US)
class ABOUT_US_Admin(admin.ModelAdmin) : 
    list_display = ("title" , "show_img" , "text" )


    def show_img(self , obj ) :  
        return format_html('<img width=50px height = 50px src="{}">'.format(obj.picture.url))
    
    show_img.short_description = "تصویر"