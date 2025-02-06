from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        reenter_password = request.POST.get('reenter-password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        # print(username,password,reenter_password,first_name,last_name,email)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name)
        user.save()
        messages.success(request, 'Sign up completed. please login')
        return redirect('login')
    return render(request, 'sign_up.html' )


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # print("hy user name is: " , user)
            # If authentication is successful, log in the user
            login(request, user)
            # print('zzzzzzzzzzzzzzzzzzzzzzzzzz')
            messages.success(request, 'You have successfully signed in!')
            return redirect('all_product')  # Replace 'home' with the name of your desired redirect page
        else:
            # print("hy there is no-user " )

            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password!')
            return render(request, 'sign_in.html')

    return render(request, 'sign_in.html' )

def logout_user(request):
    logout(request)
    return redirect('all_product' )














