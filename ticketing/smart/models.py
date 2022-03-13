from django.db import models
from accounts.models import UserProfile
# Create your models here.


class MainRequest(models.Model):

    subject = models.CharField(verbose_name='subject', blank=True, null=True, max_length=200, default="")
    descrition = models.CharField(verbose_name='descrition', blank=True, null=True, max_length=5200, default="")
    priority = models.CharField(verbose_name='priority', blank=True, null=True, max_length=200, default="")
    user = models.ForeignKey(UserProfile, verbose_name="user", on_delete=models.CASCADE, related_name="main")
    reply_user = models.ForeignKey(UserProfile, verbose_name="reply_user", on_delete=models.CASCADE, related_name="replay", blank=True, null=True)
    reply_content = models.CharField(verbose_name='reply_content', blank=True, null=True, max_length=200, default="")

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-id']
        verbose_name = 'MainRequest'
        verbose_name_plural = verbose_name