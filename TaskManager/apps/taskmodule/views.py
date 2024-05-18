from django.shortcuts import render, redirect
from .models import Task
from django.db.models import Count
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        confirmation = request.POST.get('confirmation')
        
        if confirmation == 'DELETE':
            Task.objects.filter(id__in=task_ids).delete()
            messages.success(request, "Selected tasks have been deleted.")
            return redirect('index') 
        else:
            messages.error(request, "Confirmation keyword is incorrect. No tasks were deleted.")
            return redirect('index')
    tasks = Task.objects.all()
    return render(request, 'taskmodule/index.html', {'tasks': tasks})

def tasks(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        confirmation = request.POST.get('confirmation')
        
        if confirmation == 'DELETE':
            Task.objects.filter(id__in=task_ids).delete()
            messages.success(request, "Selected tasks have been deleted.")
            return redirect('tasks') 
        else:
            messages.error(request, "Confirmation keyword is incorrect. No tasks were deleted.")
            return redirect('tasks')

    tasks = Task.objects.all()
    return render(request, 'taskmodule/taskList.html', {'tasks': tasks})

def addTask(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        description = request.POST.get('task_description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        Task.objects.create(name=name, description=description, due_date=due_date, priority=priority)
    return render(request, "taskmodule/addTask.html", {})

def updateTask(request, taskId):
    task_obj = Task.objects.get(id=taskId)
    if request.method == 'POST':
        task_name_val = request.POST.get('task_name')
        description_val = request.POST.get('task_description')
        due_date_val = request.POST.get('due_date')
        priority_val = request.POST.get('priority')
        task_obj.name = task_name_val
        task_obj.description = description_val
        task_obj.due_date = due_date_val
        task_obj.priority = priority_val
        task_obj.save()
        return redirect('task_detail', taskId=task_obj.id)
    return render(request, "taskmodule/updateTask.html", {'obj': task_obj})


def filter_tasks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        selected_genre = request.POST.get('selectedgenre')
        
        tasks = Task.objects.filter(title__icontains=string)
        
        if selected_genre != 'None':
            tasks = tasks.filter(genre=selected_genre)

        
        completed = request.POST.get('completed') 
        if completed == 'on':
            tasks = tasks.filter(completed=True)
        else:
            tasks = tasks.filter(completed=False)
        
        tasks = tasks.values('assigned_to').annotate(num_tasks=Count('assigned_to'))
        
        return render(request, 'taskmodule/taskList.html', {'tasks': tasks})
    
    return render(request, 'taskmodule/search.html', {})

def task(request, task_id):
    task_data = {
        12344321: {'id': 12344321, 'title': 'Task 1', 'description': 'Description of Task 1', 'assigned_to': 'John Doe'},
        56788765: {'id': 56788765, 'title': 'Task 2', 'description': 'Description of Task 2', 'assigned_to': 'Jane Smith'}
    }

    target_task = task_data.get(task_id)
    
    if target_task is None:
        return redirect('/tasks')
    
    context = {'task': target_task} 
    return render(request, 'taskmodule/task.html', context)
