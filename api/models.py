from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.task