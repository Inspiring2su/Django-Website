from django.shortcuts import render
from .models import Task

def index(request):
    # Return index
    return render(request, 'taskmodule/index.html')

def tasks(request):
    tasks = Task.objects.all() 
    return render(request, 'taskmodule/taskList.html', {'tasks': tasks})

def filter_tasks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        selected_genre = request.POST.get('selectedgenre')
        
        # Filter tasks based on the provided criteria
        tasks = Task.objects.filter(title__icontains=string)
        
        if selected_genre != 'None':
            tasks = tasks.filter(genre=selected_genre)
        
        return render(request, 'taskmodule/taskList.html', {'tasks': tasks})
    
    return render(request, 'taskmodule/search.html', {})

def task(request, task_id):
    # Example task data (replace with actual task retrieval logic)
    task_data = {
        12344321: {'id': 12344321, 'title': 'Task 1', 'description': 'Description of Task 1', 'assigned_to': 'John Doe'},
        56788765: {'id': 56788765, 'title': 'Task 2', 'description': 'Description of Task 2', 'assigned_to': 'Jane Smith'}
    }
    
    # Try to retrieve the task data based on the provided task ID
    target_task = task_data.get(task_id)
    
    if target_task is None:
        return redirect('/tasks')
    
    context = {'task': target_task}  # 'task' is the variable name accessible by template
    return render(request, 'taskmodule/task.html', context)
