from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  # analytical data
  done_at = models.DateTimeField(blank=True, null=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'todo'
