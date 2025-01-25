from django import forms

from site_module.models import User


class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'avatar', 'about_author', 'address']
        labels = {'نام کاربری', 'ایمیل', 'موبایل', 'تصویر پروفایل', 'درباره', 'آدرس'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل ', }),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موبایل', }),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'تصویر پروفایل', }),
            'about_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'درباره', }),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس', }),

        }
