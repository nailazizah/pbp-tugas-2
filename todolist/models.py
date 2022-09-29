from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    is_finished = models.BooleanField(null=True, blank=True)
