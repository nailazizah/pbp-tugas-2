from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


@login_required(login_url='/todolist/login/')
def todolist(request):
    data_todolist = Task.objects.filter(user=request.user)

    context = {
        'list_todo': data_todolist,
        'username': request.user.username,
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse('todolist:todolist'))  # membuat response
            response.set_cookie('last_login',
                                str(datetime.datetime.now()))  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau password tidak tepat')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def add_todo(request):
    if request.method == 'POST':
        username = request.user
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        # bonus
        is_finished = False
        Task.objects.create(user=username, date=date, title=title, description=description, is_finished=is_finished)
        response = HttpResponseRedirect(reverse("todolist:todolist"))
        return response

    return render(request, "add_todo.html")


def change_status(request, pk):
    data_todo = Task.objects.get(id=pk)
    data_todo.is_finished = not data_todo.is_finished
    data_todo.save()
    return redirect('todolist:todolist')


def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:todolist')
