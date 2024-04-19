from django.urls import path
from apps.taskmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('tasks', views.tasks, name='tasks'), 
    path('task/<int:task_id>', views.task, name='task'),  
    path('filtertasks', views.filter_tasks, name='filter_tasks'),  
]
