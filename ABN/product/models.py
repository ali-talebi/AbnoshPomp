from django.db import models
from django.urls import reverse 
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator , MaxValueValidator 

# Create your models here.

class Detail_category(models.Model) : 

    name = models.CharField(verbose_name = "نام دسته بندی" , max_length = 50 )
    slug = models.SlugField(verbose_name = "آدرس اینترنتی" , unique = True ) 
    parent = models.ForeignKey( 'Child1_detail_category' , on_delete = models.CASCADE , related_name = "Child1_detail_category" , verbose_name = "والد " )
    class Meta : 
        db_table = "Detail_category"
        vebose_name_plural = "دسته بندی های ریز محصولات" 

    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Detail_category"
        verbose_name_plural = "ریز دسته بندی ها "
    

class Child1_detail_category(models.Model) : 
    parent = models.ForeignKey( 'Product_Category' , verbose_name = "دسته بندی کلی " ,  related_name = "Product_Category_2" , on_delete = models.CASCADE )
    name = models.CharField(verbose_name = "نام ریز دسته بندی ها " , max_length = 50 ) 

    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Child1_detail_category"
        verbose_name_plural = "عنوان های ریز دسته بندی ها "



class Product_Category(models.Model) : 

    name = models.CharField(verbose_name = "عنوان دسته بندی" , max_length = 20 , unique = True   )
    slug = models.SlugField(verbose_name = "آدرس اینترنتی دسته بندی " , unique = True  ) 
    picture = models.FileField(verbose_name="تصویر دسته بندی محصولات" ,  null = True  , upload_to="Product_Category/IMAGE/")


    def __str__(self ) : 
        return self.name 
    
    class Meta : 
        db_table = "Product_Category"
        verbose_name_plural = "دسته بندی محصولات وبسایت" 
         

    



class Tags_Product(models.Model) : 
    name = models.CharField(verbose_name = "نام تگ" , max_length = 20  , unique = True  ) 
    slug = models.SlugField(verbose_name = "آدرس اینترنتی" , unique = True   )


    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Tags_Product"
        verbose_name_plural = "تگ های محصولات " 



class Information_Product(models.Model) : 


    CATEGORY_FOR_SHOW  = (
        ('featured' , 'محصولات منتخب' ) , 
        ('on-sale' , 'تخفیف خورده' ) , 
        ('most-visited' , 'پربازدید ترین')  
    )

    picture1 = models.FileField(verbose_name="تصویر 1 محصول" , upload_to="Product/IMAGE/")
    picture2 = models.FileField(verbose_name="تصویر 2 محصول" , upload_to="Product/IMAGE/")
    picture3 = models.FileField(verbose_name="تصویر 3 محصول" , upload_to="Product/IMAGE/")
    picture4 = models.FileField(verbose_name="تصویر 4 محصول" , upload_to="Product/IMAGE/")

    name = models.CharField(verbose_name = "نام محصول" , max_length = 100 ) 
    introduce = models.CharField(verbose_name = "توضیحات تک خطی" , max_length = 100 , null = True ) 
    description = RichTextField(verbose_name = "توضحیات محصول" ) 
    description_2 = RichTextField(verbose_name = "توضحیات 2  محصول" , null = True )
    category = models.ForeignKey(Product_Category , verbose_name = "دسته بندی"   , related_name = "Product_Category" , on_delete = models.CASCADE )
    Detail_category1 = models.ForeignKey(Detail_category , verbose_name = "ریز دسته بندی " , on_delete = models.CASCADE , null = True  , related_name = "Detail_category1" )
    tags = models.ManyToManyField(Tags_Product , verbose_name="تگ ها" )
    price = models.DecimalField(default =  0 , decimal_places = 0 , max_digits = 12 )

    is_sale = models.BooleanField(verbose_name = "آیا تخفیف شامل میشود " , default = False ) 
    percent_sale = models.IntegerField(verbose_name = "درصد تخفیف" , default = 0 ) 
    price2 =  models.DecimalField(default =  0 , decimal_places = 0 , max_digits = 12  , null = True , validators = [MinValueValidator(0) ] )
    marks = models.IntegerField(default = 0  , verbose_name = "امتیاز محصول" , validators = [MinValueValidator(0) , MaxValueValidator(5) ] ) 
    inventory = models.PositiveIntegerField(default = 0  , verbose_name = "موجودی محصول", validators = [MinValueValidator(0) ] )
    showing = models.CharField(verbose_name = "دسته بندی برای نمایش " , max_length = 20 , choices = CATEGORY_FOR_SHOW , null = True )

    naghd_barrasi = RichTextField(verbose_name = "نقد و بررسی محصول" , null = True ) 


    def get_absolute_url(self) : 
        return reverse("PRODUCT:Show_Detail_Product" , args=[   str(self.id) ] )

    def __str__(self ) : 
        return self.name 
    
    class Meta : 
        db_table = "Information_Product"
        verbose_name_plural = "محصولات وبسایت"


class Product_Comment(models.Model) : 
    post = models.ForeignKey(Information_Product , verbose_name = "محصول مورد نظر " , related_name = "Information_Product" , on_delete = models.CASCADE , null = True  )
    full_name = models.CharField(verbose_name = "نام و نام خانوادگی" , max_length = 100 ) 
    email = models.EmailField(verbose_name = "ایمیل " ) 
    text_comment = models.TextField(verbose_name = "متن دیدگاه" )
    creation = models.DateTimeField(verbose_name = "زمان " , auto_now_add = True , null = True )

    def __str__(self) : 
        return self.full_name 
    
    class Meta : 
        db_table = "Product_Comment"
        verbose_name_plural = "نظرات در مورد محصولات" 

