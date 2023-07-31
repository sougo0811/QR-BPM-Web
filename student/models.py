from django.conf import settings
from django.db import models
from django.utils import timezone

class StudentInfo(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=240)
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
