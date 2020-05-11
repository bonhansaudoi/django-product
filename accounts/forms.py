from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserAccount 
# from django.utils.translation import gettext_lazy as _

class UserCreationForm(forms.ModelForm): 
    first_name = forms.CharField(
        label = "Tên",  
    )
    email = forms.EmailField(
        error_messages = {
           'unique': "Email này đã được đăng kí rồi!",
        }, 
    ) 
    password1 = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput,
        min_length= 8,
    )
    password2 = forms.CharField(
        label= "Xác nhận mật khẩu",   
        widget=forms.PasswordInput
    )

    class Meta:
        model = UserAccount
        fields = ('first_name', 'email')
 
    def clean_password2(self):    
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Mật khẩu không hợp lệ!")
        return password2

    def save(self, commit=True):    
        user = super().save(commit=False)
 
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    email = forms.EmailField() 
    password = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))

class UserChangeForm(forms.ModelForm): 
    # password = ReadOnlyPasswordHashField()
    # first_name = forms.CharField(label="Tên")
    # avatar = forms.FileField(label="Hình đại diện")
    class Meta:
        model = UserAccount
        fields = ('first_name', 'email', 'avatar')

    # def clean_password(self):        
    #     return self.initial["password"]