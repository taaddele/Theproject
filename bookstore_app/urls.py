from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register, name='register'),
    path('signin',views.signin,name="signin"),
    path('download/<int:id>/',views.download_file,name="download_file"),
    path('upload',views.upload, name='upload'),
    path('create_account',views.account,name='account'),
    path('paywithyenepay',views.paywithyenepay,name='paywithyenepay'),
    path('success',views.success,name = 'success'),
    path('cancel',views.cancel, name = 'cancel')
]
      