from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def logging(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')

            return redirect('index')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logging_out(request):
    logout(request)

    return redirect('login')
