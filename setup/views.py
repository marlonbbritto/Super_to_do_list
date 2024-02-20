from django.shortcuts import render

def index(request):
    return render(request, 'to_do_list/index.html')
def login(request):
    return render(request,'users/login.html')
def register(request):
    return render(request,'users/register.html')