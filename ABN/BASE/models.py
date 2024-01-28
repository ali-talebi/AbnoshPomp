from django.db import models
from ckeditor.fields import  RichTextField
# Create your models here.





class FAQ(models.Model) : 
    q1 = models.CharField(verbose_name = "سوال 1 " , max_length = 100 ) 
    a1 =  models.CharField(verbose_name = "جواب 1 " , max_length = 100 )




    def __str__(self) : 
        return self.q1 
    
    class Meta : 
        db_table = "FAQ" 
        verbose_name_plural = "سوالات متداول"




class SLIDE_POSTER(models.Model) : 
    name = models.CharField(verbose_name = "نام عکس" , max_length = 20 ) 
    picture = models.FileField(verbose_name="تصویر" , upload_to="SLIDER/IMAGE/")

    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "SLIDE_POSTER"
        verbose_name_plural = "تصاویر اسلایدر صفحه نخست" 

        



class ABOUT_US(models.Model) : 
    title = models.CharField(verbose_name="عنوان" , max_length=100 ) 
    picture = models.FileField(verbose_name="تصویر" , upload_to="ABOUT_US/IMAGE/") 
    text = RichTextField(verbose_name = "متن " ) 


    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "ABOUT_US"
        verbose_name_plural = "درباره ما وبسایت"

    
class Teams_Member(models.Model) : 
    picture = models.FileField(verbose_name="تصویر عضو" , upload_to="Teams_Member/IMAGE/" , null = True )
    full_name = models.CharField(verbose_name="نام و نام خانوادگی" , max_length= 100 )
    positions = models.CharField(verbose_name="عنوان شغلی" , max_length= 100 ) 
    text = models.CharField(verbose_name="توضیحات تک خطی " , max_length=200 ) 


    def __str__(self) : 
        return self.full_name 
    
    class Meta : 
        db_table = "Teams_Member"
        verbose_name_plural = "اعضا برای معرفی در سایت"