from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core import serializers
from todolist.models import Task

from dataclasses import fields
import datetime
from urllib import response
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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

# @login_required(login_url='login/')
# def create_todo(request):
#     if request.method == 'POST':
#         username = request.user
#         date = datetime.datetime.now()
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         Task.objects.create(user=username, date=date, title=title, description=description)
#         # bonus
#         # is_finished = False
#         # Task.objects.create(user=username, date=date, title=title, description=description) # is_finished=is_finished)
#         response = HttpResponseRedirect(reverse("todolist:todolist"))
#         return response
#
#     return render(request, "add_todo.html")
#
# @csrf_exempt
# def add_todo(request):
#     if request.method == 'POST':
#         username = request.user
#         date = datetime.datetime.now()
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         todo = Task.objects.create(user=username, date=date, title=title, description=description) # is_finished=is_finished)
#
#         result = {
#             'fields':{
#                 'title': todo.title,
#                 'description': todo.description,
#                 'is_finished': todo.is_finished,
#                 'date': todo.date,
#             },
#             'pk': todo.pk
#         }
#         return JsonResponse(result)
#
#
# def show_json(request):
#     # data = Task.objects.all()
#     # return HttpResponse(serializers.serialize("json", data), content_type="application/json")
#     model_todo = Task.objects.filter(user = request.user)
#     return HttpResponse(serializers.serialize("json", model_todo), content_type="application/json")
#
#
#
# def change_status(request, pk):
#     data_todo = Task.objects.get(id=pk)
#     data_todo.is_finished = not data_todo.is_finished
#     data_todo.save()
#     return redirect('todolist:todolist')
#
#
# def delete(request, pk):
#     Task.objects.filter(id=pk).delete()
#     return redirect('todolist:todolist')
#
#
# # def show_json(request):
# #     # data = Task.objects.all()
# #     # return HttpResponse(serializers.serialize("json", data), content_type="application/json")
# #     model_todo = Task.objects.filter(user = request.user)
# #     return HttpResponse(serializers.serialize("json", model_todo), content_type="application/json")


@login_required(login_url='login/')
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title = title, description = description, date = datetime.date.today(), user = request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        return response
    return render(request, "createtask.html")

def show_json(request):
    model_todo = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", model_todo), content_type="application/json")

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Task.objects.create(title = title, description = description, date = datetime.date.today(), user = request.user)

        result = {
            'fields':{
                'title':todo.title,
                'date':todo.date,
                'description':todo.description,
            },
            'pk':todo.pk
        }
        return JsonResponse(result)