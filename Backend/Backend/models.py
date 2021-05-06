from django.contrib.auth.models import User


class Meta:
    model = User
    fields = ("username",)
