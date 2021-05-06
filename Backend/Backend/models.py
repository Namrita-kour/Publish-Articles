from django.db import models
from django.contrib.auth.models import User


class Meta:
    model = User
    fields = ("username",)


class Post(models.Model):
    title = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + self.author
