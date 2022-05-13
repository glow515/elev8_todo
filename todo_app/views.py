from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    '''renders the homepage when thr user is logged in'''
    my_tasks = Task.objects.all()
    return render(request,'users.html',{'my_tasks':my_tasks})

def index(request):
    '''return the page before logging in'''
    return render(request,'index.html')

def sign(request):
    '''the signup page'''
    return render(request,'sign.html')

def edit(request):
    '''the edit details page'''
    return render(request,'edit.html')

def log(request):
    '''the edit details page'''
    return render(request,'log.html')

def profile(request):
    '''the edit details page'''
    return render(request,'profile.html')

def add_task(request):
    '''add tasks from the user'''
    if request.method=='POST':
        task_passed = request.POST.get('task')
        new_task =Task()
        new_task.name = task_passed
        new_task.save()
    return redirect('home')