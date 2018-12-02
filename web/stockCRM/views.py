from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signin(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    return render(request, 'stockCRM/index.html', locals())


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def forbidden_view(request):
    return render(request, 'stockCRM/forbidden.html', locals())
