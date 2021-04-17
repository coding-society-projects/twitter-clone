from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    post_date = models.DateTimeField(default=now)
    blocked = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media', blank=True)

    def __str__(self):
        return self.content


class UserProfile(models.Model):
    image = models.ImageField(upload_to='static/profile', blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)