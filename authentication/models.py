from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('User must have a username.')

        if email is None:
            raise TypeError('User must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True,
                              db_index=True)
    username = models.CharField(verbose_name="username",
                                max_length=255,
                                unique=True,
                                db_index=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)  # manager
    is_admin = models.BooleanField(default=False)  # admin

    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        return self.email