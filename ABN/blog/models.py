from django.db import models
from ckeditor.fields import  RichTextField
from django.urls import reverse 
from .manager import Blog_Manager 
from django.utils import timezone 
# Create your models here.

class Tags(models.Model) : 
    title = models.CharField(verbose_name="عنوان تگ" , max_length=100 ) 
    slug  = models.SlugField(verbose_name="آدرس اینترنتی تگ") 

    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "Tags"
        verbose_name_plural = "تگ های پست های وبلاگ"

class Blog_Category(models.Model) : 
    title = models.CharField(verbose_name="عنوان دسته بندی" , max_length=100 )
    slug  = models.SlugField(verbose_name="آدرس اینترنتی " )

    def __str__(self) : 
        return self.title 
    

    class Meta : 
        db_table = "Blog_Category"
        verbose_name_plural = "دسته بندی پست های وبلاگ"


    
class Post(models.Model) : 

    STATUS_CHOICES = (
        ('d' , 'پیش نویس') , 
        ('p' , "انتشار")
    )


    picture = models.FileField(verbose_name="عکس پست" , upload_to="BLOG/POST/IMAGE/")
    title = models.CharField(verbose_name="عنوان پست" , max_length=100 ) 
    introduce = models.CharField(verbose_name = "معرفی پست" , max_length = 200 , null = True )
    text = RichTextField(verbose_name = "متن پست" , null = True )
    tags = models.ManyToManyField( Tags , verbose_name="تگ های این پست" )
    category = models.ForeignKey( Blog_Category , verbose_name="دسته بندی این پست" , on_delete=models.CASCADE  , related_name="Blog_Category" ) 
    creation = models.DateTimeField(verbose_name="زمان ساخت" , auto_now_add=True  , null = True ) 
    modified = models.DateTimeField(verbose_name="تغییرات زمانی" , auto_now= True , null = True ) 
    status = models.CharField(verbose_name = "وضعیت انتشار پست" , max_length = 10  , default = 'd' , choices = STATUS_CHOICES , null = True  )
    objects = Blog_Manager()
    many_visited = models.BooleanField(verbose_name = "آیا جز موارد پربازدید است ؟" , default = False , null = True ) 

    def get_absolute_url(self) : 
        return reverse("BLOG:Show_detail" , args=[str(self.id)])

    def __str__(self) : 
        return self.title 
    
    class Meta : 
        verbose_name_plural = "پست ها " 
        db_table = "Post"


        

    



class Comments(models.Model) : 
    post = models.ForeignKey( Post , verbose_name = "پست مورد نظر " , on_delete = models.CASCADE  )
    full_name = models.CharField(verbose_name = "نام و نام خانوادگی" , max_length = 100 ) 
    email = models.EmailField(verbose_name = "ایمیل" )
    text = models.TextField(verbose_name = "متن")
    created = models.DateTimeField(verbose_name = "تاریخ انتشار" , null = True   , default  = timezone.now )

    def __str__(self) : 
        return self.full_name 
    
    class Meta : 
        db_table = "Comments"
        verbose_name_plural = "کامنت ها "  