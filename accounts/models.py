from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

import uuid

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(default='a', max_length=28)

    def get_full_name(self):
        return None
    
class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=8)
