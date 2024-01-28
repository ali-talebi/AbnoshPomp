from django import forms 

class Contact_Us_Form(forms.Form) : 

    full_name = forms.CharField()
    phone = forms.CharField(max_length=11)
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    