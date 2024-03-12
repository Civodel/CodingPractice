from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
#modelos son como construkimos modelos en base de datos
#crear una clase que reprresente la clase

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=   True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['complete']
