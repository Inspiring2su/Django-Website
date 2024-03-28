from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.CharField(max_length=100)
    # You can add more fields as needed

    def __str__(self):
        return self.title




    
    