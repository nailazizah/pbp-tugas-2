from django.urls import path
from todolist.views import todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_todo

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtodo/', add_todo, name='add_todo'),
]
