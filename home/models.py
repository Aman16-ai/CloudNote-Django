from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.models import User
# Create your models here.
class NotesInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body =models.TextField()
    date = models.DateField(blank=True,null=True)
   
    