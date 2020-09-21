from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User {username} successfully created!")
            return redirect('home:landing')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            messages.success(request, "User logged in successfully!")
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('home:landing')
        else:
            context = {
                'form': form
            }
            return render(request, "users/login.html", context=context)
    else:
        form = UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context=context)
