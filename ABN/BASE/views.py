from django.shortcuts import render , redirect 
from .models import ABOUT_US , Teams_Member  , SLIDE_POSTER  , FAQ 
from blog.models import Post 
from .forms import Search_Form , Login_Form 
from django.contrib.auth import authenticate , login , logout  
from django.contrib import messages 
from .forms import SignUpForm
from product.models import Information_Product  , Product_Category 
from product.models import  Product_Category 

# Create your views here.

def FAQ_View(request) : 
    context = {
        'data':FAQ.objects.all() ,
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/faq.html' , context )


def custom_404(request, exception):
    
    return render(request, 'front/error-404.html', status=404 )


def Home(request) : 
    len_slider_count = len(SLIDE_POSTER.objects.all())
    iterable = [ _ for _ in range(len_slider_count)]
    context = {
        'top_3_posts' : Post.objects.all() , 
        'products_featured' : Information_Product.objects.filter(showing = "featured" )  ,  
        'on_sale' : Information_Product.objects.filter(showing = "on-sale" ) , 
        'most_visited' : Information_Product.objects.filter(showing = "most-visited" ) , 
        'product_category' : Product_Category.objects.all() , 
        'slider' : SLIDE_POSTER.objects.all() , 
        'len_slider' : iterable , 
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/index.html' , context )

def about_us(request) : 
    context = {
        'data' : ABOUT_US.objects.all().first() , 
        'info_team' : Teams_Member.objects.all() , 
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/about.html' , context )


def search(request) : 

    if request.method == "GET" : 
        q = request.GET.get("text")
        

    data = Post.objects.all().filter(title__icontains = q )

    if len(data) : 
        name_tamplate = 'front/blog.html'

    else : 
        name_tamplate ="front/error-404.html"
    
    return render(request , name_tamplate , {'data':data })


def login_user(request) : 
    if request.method == "POST" : 
        form = Login_Form(request.POST)
        if form.is_valid() : 
            username1 = form.cleaned_data["username"]
            password1 = form.cleaned_data["password"]

            user = authenticate(request , username = username1 , password = password1 )

            if user : 
                login(request , user )
                messages.success(request , f"{user.first_name}-{user.last_name} با موفقیت وارد شدید" , "success" )
                return redirect("BASE_app:Home")
            else : 
                messages.error(request , "با موفقیت خارج شدید" , "error" ) 
                return redirect("BASE_app:Home")
    else : 
        form = Login_Form()

    return render(request , 'front/login.html' , {'form':form} )





def logout_user(request) : 
    logout(request)
    messages.success(request , "با موفقیت خارج شدید" , "success" )
    return redirect("BASE_app:Home")

    

def Register(request) : 
    if request.method == "POST" : 
        form = SignUpForm(request.POST)
        if form.is_valid() : 
            user = form.save()
            login(request , user )
            messages.success(request , "با موفقیت ثبت نام شدید" , "success")
            return redirect("BASE_app:Home")
        
    else : 
        form = SignUpForm()

    return render(request , 'front/register.html' , {'form':form})