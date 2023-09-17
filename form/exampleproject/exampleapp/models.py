from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    # user=models.ForeignKey(Member , on_delete=models.SET , null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)