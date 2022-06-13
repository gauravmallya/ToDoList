from django.db import models

# Create your models here.

class Tasks(models.Model):
    TaskID = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=200)
    TaskCompletion = models.BooleanField()
