from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import (
    UserForm,
    EditUserForm,
)
from stockCRM.decorators import (
    is_anonymous,
    is_warehouse_manager
)


@is_warehouse_manager
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', locals())


@is_warehouse_manager
def user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', locals())


@is_warehouse_manager
def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('user_list')
    return render(request, 'users/user_create.html', locals())


@is_warehouse_manager
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/user_edit.html', locals())
