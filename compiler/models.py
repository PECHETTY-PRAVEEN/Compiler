from django.db import models

# Create your models here.
class PythonCode(models.Model):
    code=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)