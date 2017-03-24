from django.shortcuts import render,redirect

def index(request):
    return render(request, 'wish_list/index.html')

def logout(request):
    return redirect('users:my_index')

def add(request):
    return render(request, 'wish_list/create.html')

def create(request):
    return redirect('wish:my_index')


# Create your views here.
