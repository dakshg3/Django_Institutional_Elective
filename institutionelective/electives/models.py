from django.db import models
from datetime import datetime, timezone
from django.utils import timezone
import pytz

# Create your models here.
class Choices(models.Model):
    timezone.activate(pytz.timezone("Asia/Kolkata"))
    usn = models.CharField(max_length=10, primary_key=True)
    choice1 = models.CharField(max_length=40)
    choice2 = models.CharField(max_length=40)
    choice3 = models.CharField(max_length=40)
    choice4 = models.CharField(max_length=40)
    choice5 = models.CharField(max_length=40)
    cur_time = models.CharField(max_length=15, default=datetime.now, blank=True)


class Options(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)

class AdminLogin(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pass = models.CharField(max_length=20, null=False)

class timer(models.Model):
    hrs=models.CharField(max_length=20,default=10)
    mins=models.CharField(max_length=20,default=30)

class allocated(models.Model):
    usn = models.CharField(max_length=15, primary_key=True)
    sub = models.CharField(max_length=40)
