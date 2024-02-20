from django.urls import path

from to_do_list.views import index, login, register,logout, register_task

urlpatterns = [
    path('', index, name= 'index'),
    path('login', login, name= 'login'),
    path('register', register, name= 'register'),
    path('logout', logout, name= 'logout'),
    path('register_task', register_task, name= 'register_task'),
    
]