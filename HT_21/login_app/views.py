from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect(main)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(
                username=form_data['username'],
                password=form_data['password']
            )
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse(f'{user.username} is banned!')
            else:
                form.add_error(None, '')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login_app/login.html', context)


def main(request):
    return render(request, 'login_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
