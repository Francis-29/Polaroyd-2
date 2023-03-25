from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('You have not provided a valid user_id')

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, user_id=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(user_id, password, **extra_fields)
     
     
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=64, unique=True, primary_key=True)
    name = models.CharField(max_length=128)
    bio = models.CharField(max_length=255, default='')
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/avatar.png')
    profile_banner = models.ImageField(upload_to='profile_banner/', blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.name
        