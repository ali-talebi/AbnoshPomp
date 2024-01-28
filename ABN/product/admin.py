from django.contrib import admin
from .models import Detail_category ,  Child1_detail_category , Product_Comment , Information_Product , Tags_Product , Product_Category 
from django.utils.html import format_html 

# Register your models here.


@admin.register(Child1_detail_category)
class Child1_detail_category_Admin(admin.ModelAdmin) : 
    list_display = ("name" , "parent"  ) 
    list_editable = ["parent" , ]




@admin.register(Detail_category)
class Detail_category_Admin(admin.ModelAdmin) : 
    list_display = ("name" , "slug" , "parent" ) 
    prepopulated_fields = {"slug" : ("name" , "parent" , )}
    list_editable = ["parent" , ]




@admin.register(Product_Comment)
class Product_Comment_Admin(admin.ModelAdmin) : 
    list_display = ("full_name" , "email" , "post" , "creation" , "text_comment" ) 
    search_fields = ("full_name" , "text_comment" , "email" )
    list_filter = ["email" , ] 




@admin.register(Information_Product)
class Information_Product_Admin(admin.ModelAdmin) : 
    list_display = ("name" , "showing" , "show_img" , "Detail_category1" , "category" , "show_tags"  , "price" , "is_sale"  , "percent_sale" , "marks"  , "inventory"  ) 
    list_editable = ["showing" , "Detail_category1" ,  "category" ]

    def show_tags(self , obj )  : 
        return ' , '.join([i.name for i in obj.tags.all() ])
    

    show_tags.short_description = "تگ های محصول" 

    def show_img(self , obj ) : 
        return format_html('<img width=50px height = 50px src="{}">'.format(obj.picture1.url))



@admin.register(Tags_Product)
class Tags_Product_Admin(admin.ModelAdmin) : 
    list_display  = ("name" , "slug"  )
    prepopulated_fields = {'slug':('name' , )}


@admin.register(Product_Category)
class Product_Category_Admin(admin.ModelAdmin) : 
    list_display = ( "name" , "slug"  )
    prepopulated_fields = {'slug':('name' , )}

