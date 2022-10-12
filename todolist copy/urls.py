from django.urls import path
from todolist.views import todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_todo
# from todolist.views import change_status
# from todolist.views import delete
# # from todolist.views import todolist_ajax
# from todolist.views import show_json
from todolist.views import create_todo
from todolist.views import show_json
# from todolist.views import show_newtask
# from todolist.views import add_task


app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtodo/', add_todo, name='add_todo'),
    # path('isfinished/<int:pk>', change_status, name='change_status'),
    # path('delete/<int:pk>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    # path('add/', add_task, name='add_task'),
    # path('create-task/', show_newtask, name='show_newtask'),
    path('createtodo/', create_todo, name='create_todo'),
    # path('ajax/', todolist_ajax, name='todolist_ajax'),
]