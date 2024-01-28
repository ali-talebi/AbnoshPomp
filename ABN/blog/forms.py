from django import forms 

class Comments_Form(forms.Form) : 
    
    full_name = forms.CharField()
    email = forms.EmailField()
    text_comment = forms.CharField(widget=forms.Textarea)
    