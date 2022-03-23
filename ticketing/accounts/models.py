from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):

    mpassword = models.CharField(verbose_name='password', blank=True, null=True, max_length=200, default="")
    email = models.CharField(verbose_name='email', blank=True, null=True, max_length=200, default="")
    is_teacher = models.BooleanField(verbose_name='is teacher?', default=False)
    have_active = models.BooleanField(verbose_name='is active?', default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = 'user manage'
        verbose_name_plural = verbose_name