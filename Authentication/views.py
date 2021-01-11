from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
# Create your views here.

def login_view(request,*args,**kwargs):
    '''
    Log In Page View
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home_view')
    return render(request,'LogIn_Page.html')

def logout_view(request,*args,**kwargs):
    print('logout')
    logout(request)
    return render(request,'LogIn_Page.html')

def register(request):
    if request.method == 'GET':    
        context = {'form':CustomUserCreationForm}
        return render(request,'registration/register.html',context,status=200)
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request,user)
            return redirect('room_list_view')
    return render(request,'registration/register.html',context,status=200) 