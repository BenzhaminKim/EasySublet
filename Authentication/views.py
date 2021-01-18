from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
import logging
# Create your views here.

def login_view(request,*args,**kwargs):
    '''
    Log In Page View
    '''
    logger = logging.getLogger("loggers")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            logger.info(user)
            return redirect('home_view')
    logger.info(request)
    return render(request,'LogIn_Page.html')

def logout_view(request,*args,**kwargs):
    logger = logging.getLogger("loggers")
    logout(request)
    logger.info(request)
    return render(request,'LogIn_Page.html')

def register(request):
    logger = logging.getLogger("loggers")
    if request.method == 'GET':    
        context = {'form':CustomUserCreationForm}
        logger.info(context)
        return render(request,'registration/register.html',context,status=200)
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request,user)
            logger.info(user)
            return redirect('room_list_view')
    logger.info(request)
    return render(request,'registration/register.html',context,status=200) 