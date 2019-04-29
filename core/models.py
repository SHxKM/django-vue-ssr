# Create your models here.
from django.db import models


# Create your models here.
class ToDoItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)