from django.db import models

# Create your models here.

class Queras(models.Model):
    name = models.CharField(max_length=255)

class Tickets(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Queras, on_delete=models.DO_NOTHING)