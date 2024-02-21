from django.urls import path

from to_do_list.views import delete_task, done_task, edit_task, index, login, register,logout, register_task

urlpatterns = [
    path('', index, name= 'index'),
    path('login', login, name= 'login'),
    path('register', register, name= 'register'),
    path('logout', logout, name= 'logout'),
    path('register_task', register_task, name= 'register_task'),
    path('edit-task/<int:tasks_id>', edit_task, name= 'edit_task'),
    path('delete-task/<int:tasks_id>', delete_task, name= 'delete_task'),
    path('done-task/<int:tasks_id>', done_task, name= 'done_task'),
    
]