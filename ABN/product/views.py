from django.shortcuts import render , redirect 
from .models import Information_Product , Product_Comment , Product_Category 
from .forms import Product_Comment_Form 
from django.contrib import messages 
# Create your views here.




def show_total_detail_category_product(request , vorodi ) : 
    context = {
        'detail_category' : Information_Product.objects.all().filter(Detail_category1__slug = vorodi ) , 
        'Product_Category' : Product_Category.objects.all()  , 
    }
    return render( request  , 'front/products2.html' , context )



def show_product_base_category(request , vorodi ) : 
    context = {
        'product':Information_Product.objects.all().filter(category__slug = vorodi  ) , 
        'Product_Category' : Product_Category.objects.all() 
    }
    return render(request , 'front/products.html' , context ) 





def Show_Detail_Product(request ,  id ) : 
    data = Information_Product.objects.get( id = id )
    form = Product_Comment_Form()
    if request.method == "POST" : 
        form = Product_Comment_Form(request.POST)

        if form.is_valid() : 
            new_full_name = form.cleaned_data["full_name"]
            new_email = form.cleaned_data["email"]
            new_text_comment = form.cleaned_data["text_comment"]
            model1 = Product_Comment( post = data , full_name = new_full_name , 
                            email = new_email , 
                            text_comment = new_text_comment  )
            
            model1.save()
            messages.success(request , f"{new_full_name} دیدگاه شما با موفقیت ثبت شد" , "success") 
            return redirect("/")
        else : 
            messages.error(request , "مشکلی در ثبت دیدگاه وجود دارد " , "error" ) 

            




    
    
    context = {
        'detail_product' : data  , 
        'related_product' : Information_Product.objects.all()  , 
        'comments_product' : Product_Comment.objects.all().filter(post = data ) , 
        'form' : form , 
        'len_comment' : len( Product_Comment.objects.all().filter(post = data ) ) , 
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/product.html' , context )