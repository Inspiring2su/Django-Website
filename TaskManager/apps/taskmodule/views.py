from django.shortcuts import render
from .models import Task
from django.db.models import Count

def index(request):
    return render(request, 'taskmodule/index.html')

def tasks(request):
    tasks = Task.objects.all() 
    return render(request, 'taskmodule/taskList.html', {'tasks': tasks})

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
