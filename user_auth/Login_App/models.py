from django.db import models
from django.contrib.auth.models import User


# My models here.
class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    #function to return string
    def __str__(self):
        return self.user.username
