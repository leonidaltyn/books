from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=20, blank=True)
    last_name=models.CharField(max_length=20, blank=True)
    email=models.EmailField(unique=True)
CustomUser.groups.field.remote_field.related_name = 'customuser_groups'
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_permissions'