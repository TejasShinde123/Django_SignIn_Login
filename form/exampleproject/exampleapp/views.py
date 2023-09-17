from django.shortcuts import render,redirect
from . import templates
from exampleapp.models import Member
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth , User

# Create your views here.
def index(request):        
    return render(request , 'index.html')

def signup(request):
    if request.method =="POST" :
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Member.objects.filter(email=email).exists():
            messages.warning(request, 'email already exists')
            return redirect('/signup/')
        
        else:
            member=Member(name = name, email = email , password = password)
            member.save()
            messages.success(request, 'the user added succsessfully')
            return redirect('/login/')
        

    return render(request , 'signup.html')


def login_view(request):
    if request.method=='POST':
        # Assuming you have a Email and password from user input
        name = request.POST['name']
        password1 = request.POST['password']

        # Authenticate the user
        user = auth.authenticate(request, name=name, password=password1)

        if user is not None:
            # Password is correct, and user is authenticated.
            auth.login(request, user)
            # Redirect to a success page or return an appropriate response.
            return redirect('/demo/')
        else:
            # Invalid Email or password.
            # You can render a login form with an error message here.
            messages.info(request, 'Credentials Invalid')
            return render(request, 'login.html')

    # If the request method is not POST or it's the initial GET request, render the login form.
    return render(request, 'login.html')


def next(request):
    return render(request,'next.html' )

def demo (request):
    messages.success(request, 'this is not good')
    return render(request, 'demo.html')