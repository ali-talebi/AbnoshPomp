from django.shortcuts import render
from .models import Post , Comments 
from .forms import Comments_Form 
from product.models import Information_Product 
from django.contrib import messages 
from django.utils import timezone 
from product.models import  Product_Category 


# Create your views here.



def Show_Blog(request) : 
    context = {
        'posts':Post.objects.all() , 
        'many_visited_post' : Post.objects.all().filter(many_visited = True ) , 
        'many_visited_product' : Information_Product.objects.all().filter(showing = 'most-visited') , 
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/blog.html' , context )


def Show_detail(request , id ) : 
    comments = Comments_Form()
    post1 = Post.objects.get( id = id )
    if request.method == "POST" : 



        
        form = Comments_Form(request.POST)
        if form.is_valid() : 
            newfull_name = form.cleaned_data["full_name"]
            newemail = form.cleaned_data["email"]
            newtext_comment = form.cleaned_data["text_comment"]


            
            model1 = Comments(post = post1 , full_name = newfull_name , email = newemail , 
                              text = newtext_comment , created = timezone.now() )
            model1.save()
            messages.success(request , "با موفقیت ثبت شد " , "success")

        else : 
            comments = Comments_Form()
            messages.error(request , " متاسفانه ثبت نشد " , "error")


    else : 
        form = Comments_Form()



    context = {
        'detail_post' : post1 , 
        'comments' : form , 
        'comments' : Comments.objects.filter(post = post1 ) , 
        'many_visited_post' : Post.objects.all().filter(many_visited = True ) , 
        'many_visited_product' : Information_Product.objects.all().filter(showing = 'most-visited') , 
        'Product_Category' : Product_Category.objects.all() , 

    } 
    return render(request , 'front/blog-post.html' , context  )