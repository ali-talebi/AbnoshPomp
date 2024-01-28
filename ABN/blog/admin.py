from django.contrib import admin
from django.utils.html import format_html 
from .models import * 
from django.contrib import messages 

# Register your models here.


@admin.register(Tags)
class Tags_Admin(admin.ModelAdmin) : 
    list_display = ('title'  , 'slug')
    prepopulated_fields = {'slug' : ('title' , )}


@admin.register(Blog_Category)
class Blog_Category_Admin(admin.ModelAdmin) : 
    list_display = ("title" , "slug" ) 
    prepopulated_fields = {'slug' : ('title' , )}


@admin.register(Post)
class Post_Admin(admin.ModelAdmin) : 
    list_display = ("title"  , "show_img" , 'status'  , "many_visited" , "show_tags"  , "category" , "creation" , "modified" , "introduce" )  
    
    
    def show_img(self , obj ) : 
        return format_html('<img width=50px height=50px src="{}">'.format(obj.picture.url))
    show_img.short_description = "تصویر"
    
    list_editable = ['status' , 'many_visited'  ]
    actions = ['public' , 'Change_many_visit_True' ]

    def public(self, request , queryset  ) : 
        result = queryset.update(status = 'p' ) 
        self.message_user(request , f"{result}  پست با موفقیت منتشر شد ")
        
    public.short_description = "منتشر کردن پست"


    def Change_many_visit_True(self , request , queryset ) : 
        result = queryset.update(many_visited = True )
        self.message_user(request , f"{result} پست با موفقیت جز پست های پربازدید قرار گرفت")

    Change_many_visit_True.short_description = "فعال کردن پربازدید"
    


    def show_tags(self , obj ) : 
        return ' , '.join([i.title for i in obj.tags.all() ])
    
    show_tags.short_description = "تگ های مورد نظر "


@admin.register(Comments)
class Comments_Admin(admin.ModelAdmin) : 
    list_display = ("post" , "full_name" , "email" )