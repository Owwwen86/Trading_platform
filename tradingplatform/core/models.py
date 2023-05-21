from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['is_active']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
