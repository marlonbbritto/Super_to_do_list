from django.shortcuts import render, redirect
from to_do_list.forms import LoginForms, RegisterForms, TaskForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from to_do_list.models import Tarefas


def index(request):
    form = TaskForms()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForms(request.form)
        user=request.user.username
        tasks= Tarefas.objects.filter(user=user)         
    else:
        messages.error(request, 'Necessario fazer Login')
        return redirect('login' )
    return render(request,'to_do_list/index.html',{'form':form,"tasks":tasks})  
def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['user_name'].value()
            password = form['password'].value()
        
        user = auth.authenticate(
            request,
            username = name,
            password = password              
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{name} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')        
    return render(request,'users/login.html', {'form':form})
def register(request):
    form = RegisterForms()
    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password'].value() != form['password2'].value():
                return redirect('register')
            name = form['user_name'].value()
            email = form['email'].value()
            password = form['password'].value()
           
        
            if User.objects.filter(username=name).exists():
                messages.error(request,'Usuário já existente')
                return redirect('register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request,'Cadastro efetuado com sucesso!')
            return redirect('login')
    return render(request,'users/register.html',{'form':form})
def logout(request):
    auth.logout(request)
    messages.success(request,'Logout efetuado')
    return redirect('login')
def register_task(request):
    form = TaskForms
    if request.method == 'POST':        
        form = TaskForms(request.POST)
        if form.is_valid():
            form.instance.user =request.user            
            form.save()
            messages.success(request,'Task cadastrada com sucesso')
    return redirect('index')
def delete_task(request):
    pass
def edit_task(request, tasks_id):
    task = Tarefas.objects.get(id=tasks_id)
    form = TaskForms(instance=task)

    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'task editada com sucesso')
            return redirect('index')
    return render(request,'to_do_list/edit_task.html',{'form':form,'tasks_id':tasks_id})
    pass
