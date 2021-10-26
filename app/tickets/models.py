from django.db import models

# Create your models here.

class Quera(models.Model):
    name = models.CharField(max_length=255)

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Quera, on_delete=models.DO_NOTHING)