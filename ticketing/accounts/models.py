from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):

    avatar = models.ImageField(blank=True, null=True, verbose_name='头像', upload_to="avatar/")
    mpassword = models.CharField(verbose_name='密码', blank=True, null=True, max_length=200, default="")
    mobile = models.CharField(verbose_name='手机号', blank=True, null=True, max_length=200, default="")
    location = models.CharField(verbose_name='所属位置', blank=True, null=True, max_length=200, default="")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name