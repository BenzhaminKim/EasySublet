from django.shortcuts import render

# Create your views here.
def log_In_view(request,*args,**kwargs):
    '''
    Log In Page View
    '''
    print("Log In")
    return render(request,'Authentication/LogIn_Page.html')


