from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def logging(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser is False:
                login(request, user)
                messages.success(request, 'Login successful.')
                request.session['account_id'] = user.account.social_media_id.platform.account_id

                return redirect('index')

            else:
                messages.error(request, 'This is a Superuser')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logging_out(request):
    logout(request)

    return redirect('login')


def profile_detail(request):
    return render(request, 'profile_detail.html')
