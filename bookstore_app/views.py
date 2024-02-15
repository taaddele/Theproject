from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from .models import BookUploadModel
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
import os
import os.path
from django.conf import settings
# Create your views here.
def home(request):
    data = BookUploadModel.objects.all()
    return render(request,"home.html",{'data':data}) 
def register(request):
    form = registerForm()
    if request.method=='POST':
        form = registerForm(request.POST)
        category = request.POST['category']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():       
            user = User.objects.create_user(first_name = first_name,
            last_name=last_name,email=email,username=username,password=password1)
            user.save()
            return redirect('home')             
        return render(request, 'register.html', {
            'form': form,
        })
    else:
        return render (request, 'register.html', {
            'form': form
        })

def upload(request):
    form = UploadForm()
    if request.method=='POST':
        # POST, return form with data from the request
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():   
           form.save()
           form = UploadForm()
           return render(request,"upload.html",{'form':form})          
    else:
        # GET, return empty form
        form=UploadForm()
    return render(request,'upload.html',{'form':form})
def account(request):
    form ="rest of us"
    return render(request,'account.html',{'form':form})
def signin(request):
    form = SignInForm()
    message = ''
    if request.method=='POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                message = f'hello {user.username}! you have been logged in '
            else:
                message = 'login failed'
    return render(request,"login.html",context = {'form':form,'message':message})
def download_file(request,id):
    file_to_be_downloaded = BookUploadModel.objects.get(id=id)
    response = HttpResponse(file_to_be_downloaded.Book_file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{file_to_be_downloaded.Book_file.name}"'
    return response
def paywithyenepay(request):
    return render(request,'paywithyenepay.html')
def success(request):
    return render(request,"success.html")
def cancel(request):
    return render(request,"cancel.html")
    
    

