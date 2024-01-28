from django.shortcuts import render , redirect 
from .models import Information_Company , Send_Message 
from .forms import Contact_Us_Form 
from django.contrib import messages 
from product.models import  Product_Category 


# Create your views here.


def Conatc_Us_View(request) : 
    form = Contact_Us_Form()

    if request.method == "POST" : 
        form = Contact_Us_Form(request.POST)

        if form.is_valid() : 
            new_full_name = form.cleaned_data["full_name"]
            new_phone = form.cleaned_data["phone"]
            new_email = form.cleaned_data["email"]
            new_subject = form.cleaned_data["subject"]
            new_text = form.cleaned_data["text"]

            model_form = Send_Message(full_name = new_full_name , phone = new_phone , 
                        email = new_email , subject = new_subject , text = new_text  )
            model_form.save()
            messages.success(request , "پیام شما با موفقیت ثبت شد " , "success")

            return redirect("contact_us:Conatc_Us_View")
        
        else : 
            messages.error(request , "پیام شما با مشکل مواجهه شده است " , "error")
            return redirect("contact_us:Conatc_Us_View")
    

        


    context = {
        'data_company' : Information_Company.objects.all().first()  , 
        'form' : form , 
        'Product_Category' : Product_Category.objects.all() , 

    }
    return render(request , 'front/contact.html' , context )