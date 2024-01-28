from django.db import models

# Create your models here.



class Information_Company(models.Model) : 

    address = models.CharField(verbose_name = "آدرس فروشگاه" , max_length = 100 ) 
    location = models.CharField(verbose_name = "آدرس از روی نقشه" , max_length = 200 , null = True )
    tel1 = models.CharField(verbose_name = "تلفن 1 " , max_length = 11 ) 
    tel2 = models.CharField(verbose_name = "تلفن 2 "  , max_length = 11 ) 

    email = models.EmailField(verbose_name = "ایمیل "  ) 


    def __str__(self ) : 
        return self.email 
    
    class Meta : 
        db_table = "Information_Company"
        verbose_name_plural = "آدرس و مشخصات شرکت" 


class Send_Message(models.Model) : 

    STATUS_CHOICES = (
        ('N' , "در انتظار پاسخ" ) , 
        ('Y' , "پاسخ داده شده" )   , 
        ('C' , "در حال رسیدگی" )  , 
    )

    full_name = models.CharField(verbose_name = 'نام و نام خانوادگی' , max_length = 100 ) 
    phone = models.CharField(verbose_name =  "تلفن " , max_length = 11 ) 
    email = models.EmailField(verbose_name = "ایمیل" ) 
    subject = models.CharField(verbose_name = "موضوع پیام" , max_length = 50  , null = True ) 
    text  = models.TextField(verbose_name = "متن پیام" ) 


    created = models.DateTimeField(verbose_name = "زمان ساخت" , auto_now_add = True ) 
    status  = models.CharField(verbose_name = "وضعیت رسیدگی به پیام" , max_length = 10  , choices = STATUS_CHOICES , default = "N" )   


    class Meta : 
        db_table = "Send_Message" 
        verbose_name_plural = "پیام های ارسال شده از طرف فرم ارتباط با ما" 

