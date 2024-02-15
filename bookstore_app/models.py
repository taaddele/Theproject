from django.db import models
from django import forms
from django.core.validators import MinValueValidator
import os
from django_resized import ResizedImageField

class BookUploadModel(models.Model):
    book_title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    cover_page= ResizedImageField(size=[200, 600],upload_to="static/images")
    Book_file = models.FileField()
    author_name = models.CharField(max_length=100)
    price= models.IntegerField(validators=[MinValueValidator(5)])
    published_date = models.DateField()
    file_size = models.BigIntegerField(null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.Book_file:
            self.file_size = self.Book_file.size
        super().save(*args, **kwargs)
    class Meta:
         verbose_name_plural = 'Books'
    def __str__(self):
         return f"Book ({self.id})"
    def clean_photo(self):
        image_file = self.cleaned_data.get('cover_page')
        if not image_file.cover_page.endswith(".jpg"):
            raise forms.ValidationError("Only .jpg image accepted")
        return image_file

     #def __init__(self,*args,**kwrargs):
         # super().__init__(*args,**kwrargs)
         # self.fields['cover_page'].widget.attrs.update({'class':'form-control'})
         # self.fields['Book_file'].widget.attrs.update({'class':'form-control'})
         # self.fields['Isbn'].widget.attrs.update({'class':'form-control'})
         # self.fields['price'].widget.attrs.update({'class':'form-control'})
         # self.fields['published_date'].widget.attrs.update({'class':'form-control'})




