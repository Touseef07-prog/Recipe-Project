from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm, UserLoginForm 
from django.views.generic import View




class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'signup_form': UserForm(),
            
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        context = {
            'signup_form': user_form,  
        }
        if user_form.is_valid():
            user_form.save()
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('cocktail:home')
        return render(request, 'users/register.html', context=context)

