import phonenumbers
from django import forms
from .models import BookUploadModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from phonenumber_field.phonenumber import PhoneNumber
username_validator = UnicodeUsernameValidator()


class registerForm(UserCreationForm):
    choices = ((1,"author"),(2,"Reviewer"))
    category = forms.ChoiceField(choices=choices,label='Choose Role:',widget=forms.Select(
        attrs={'class':'form-control'}
    ))
    first_name = forms.CharField(label="First Name:",max_length=50,widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    last_name = forms.CharField(label="Last Name:",max_length=50,widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    username = forms.CharField(
        label=_('Username:'),
        max_length=50,
        validators=[username_validator],
        error_messages={'unique': _(
            "A user with that username already exists.")},
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    email = forms.EmailField(label='Email:',required=True,widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    password1 = forms.CharField(label=_('password:'),
                                widget=forms.PasswordInput(
                                    attrs={'class':'form-control'}
                                )
                                )
    password2 = forms.CharField(label=_('password again'), widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    class Meta:
        model = User
        fields = ('category','first_name', 'last_name', 'username','email','password1','password2')
class SignInForm(AuthenticationForm):
    username = forms.CharField(label=_(
        'Username'), max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password',)
class UploadForm(forms.ModelForm):
     class Meta:
          model = BookUploadModel
          fields = ['book_title','category','cover_page','Book_file','author_name',
                    'price','published_date']
          CHOICES = ((1,'Arts & Music'),(2,'Biographies'),(3,'Business'),(4,'Comics'),
                     (5,'Computer & Tech'),(6,'Cooking'),(7,'Edu & Reference'),
                     (8,'Entertainment'),(9,'Health & Fitness'),(10,'History'),
                     (11,'Gobbies & Crafts'),(12,'Literature & Fiction'),
                     (13,'Medical'),(14,'Mysteries'),(15,'Religion'),
                     (16,'Romance'),(17,'Science & Math'),(18,'Self-Help'),
                     (19,'Social Science'),(20,'Sports'),(21,'Travel'),
                     )
          widgets = {
               'author_name':forms.TextInput(attrs={'class':'form-control'}),
               'book_title':forms.TextInput(attrs={'class':'form-control'}),
               'category':forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
               'cover_page':forms.ClearableFileInput(attrs={'class':'form-control'}),
               'Book_file':forms.ClearableFileInput(attrs={'class':'form-control'}),
               'price':forms.NumberInput(attrs={'class':'form-control'}),
               'published_date':forms.DateInput(attrs={'class':'form-control',
                                                       'placeholder':'yyyy-mm-dd'})
          }


