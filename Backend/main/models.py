from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Post_list')


class Meta:
    model = User
    fields = ("username",)


class Post(models.Model):
    title = models.CharField(max_length=240)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="pictures/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=240, default='Better Programming')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('Post_list')
