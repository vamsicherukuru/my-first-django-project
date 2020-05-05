from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    display_pic = models.ImageField(upload_to = 'display_pictures',blank= True)
    linkedIn_url =  models.URLField(blank=True)

    def __str__(self):
        return self.user.username 
