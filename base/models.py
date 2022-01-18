from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    clientname = models.CharField(max_length=200)
    task = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clientname

    class Meta:
        order_with_respect_to = 'user'
