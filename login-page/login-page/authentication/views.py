from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here.


def home(request):
    return render(request , 'authentication/index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myUser = User.objects.create_user(username , email , pass1)
        myUser.first_name = fname
        myUser.last_name = lname

        myUser.save()

        messages.success(request , "Your account has been successfully created")

        return redirect('signin')


    return render(request , 'authentication/signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username , password=pass1)

        if user is not None:
            login(request , user)
            fname = user.first_name
            return render(request , "authentication/index.html" , {'fname': fname})

        else:
            messages.error(request , "Bad Credentials")
            return redirect('home')



    return render(request , 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request , "Logged out successfully!!")
    return redirect('home')
