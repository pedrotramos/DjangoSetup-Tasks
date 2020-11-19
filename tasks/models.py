from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    description = models.CharField(max_length=500)
