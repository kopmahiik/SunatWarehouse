from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_resized import ResizedImageField

from user.enums import UserTypeChoices


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.user_type = 'user'
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.user_type = 'user'
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(
        verbose_name='Имя',
        max_length=255,
        blank=True
    )
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    )
    user_type = models.CharField(
        'Тип пользователя',
        max_length=25,
        choices=UserTypeChoices,
        default=UserTypeChoices.ADMIN,
    )
    last_login = models.DateTimeField(
        verbose_name='Последний вход:',
        blank=True,
        null=True
    )
    avatar = ResizedImageField(
        upload_to="uploads/users/avatars/",
        size=[400, 400],
        crop=['middle', 'center'],
        blank=True,
        null=True,
        verbose_name="Фото пользователя"
    )

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
