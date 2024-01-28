from django.db import models
from django.contrib.auth.models import  AbstractBaseUser 
# Create your models here.



class Custom_User(AbstractBaseUser) : 

    email = models.EmailField(verbose_name = "ایمیل" , unique = True , max_length = 255 )
    phone_number = models.CharField(verbose_name = "تلفن همراه" , max_length = 11  , unique = True ) 
    full_name = models.CharField(verbose_name = "نام و نام خانوادگی" , max_length = 100 )

    USERNAME_FIELDS = ['phone_number'] 
    REQUIRED_FIELDS = ['email' , 'full_name' ] 
    is_active = models.BooleanField(verbose_name = "آیا کاربر فعال است ؟ " , default = True )
    is_admin = models.BooleanField(Verbose_name = "آیا ادمین است ؟ " , default = False ) 


    def has_perms(self , perm , obj = None  ) :
        return True 

    def __str__(self) : 
        return self.email 

    def has_module_perm(self ) : 
        return True 
    @property 
    def is_staff(self) : 
        return self.is_admin 
