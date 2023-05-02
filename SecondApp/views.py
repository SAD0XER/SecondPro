from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    # if request.user.is_anonymous:
    #     return redirect("/signup")
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Re-Obsserve all the functions below.
def signUp(request):
    if request.method == 'POST':
        # Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        # Checks for Errorneous Inputs.
        # Username must be under 10 characteres.
        if len(username) > 10:
            messages.error(request, "Username must be uder 10 characters!")
            return redirect("/home")

        # Username contains only alphanumeric characteres.
        if not username.isalnum():
            messages.error(request, "Username contains only alphanumeric characters!")
            return redirect("/home")

        # Both password must be match.
        if pwd1 != pwd2:
            messages.error(request, "Password doesn't match!")
            return redirect("/home")

        # Create User
        MyUser = User.objects.create_user(username, email, pwd1)
        MyUser.first_name = fname
        MyUser.last_name = lname
        MyUser.save()
        messages.success(
            request, "Your account has been successfully created! Happy Now?")
        return redirect('/home')
    else:
        # Add 404 error page, and see how it works.
        return HttpResponse('ERROR 404: Page Not Found')


def LogIn(request):
    if request.method == 'POST':
        # Get the post parameters
        Username = request.POST['Username']
        Pass = request.POST['Pass']

        user = authenticate(username=Username, password=Pass)

        if user is not None:
            login(request, user)
            messages.success(request, "Succsefully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again!")
            return redirect('home')
    return HttpResponse('ERROR 404: Page Not Found')

def LogOut(request):
    logout(request)
    messages.success(request, "Succsefully Logged Out!")
    return redirect("home")
