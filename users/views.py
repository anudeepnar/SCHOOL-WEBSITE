from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


def RegisterUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            #login(request, user)
            messages.success("Your account is created!")
            return redirect(request,'curriculum:home')
            #return render(request, 'curriculum/home')
        messages.error(request, "Unsuccessful registration. Invalid information.")

    else:
        form = UserForm()

    context = {
            'form': form
        }
    return render(request, 'users/registration.html', context)

def SigninUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('curriculum:home')

        else:
            return HttpResponse("Please use correct id and password")

    else:
        return render(request, 'users/signin.html')

@login_required
def LogoutUser(request):
    logout(request)
    return render(request, 'users/logout.html')
