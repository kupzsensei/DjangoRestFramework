from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField(auto_now_add=True)
    bio = models.CharField(max_length=200 , blank=True , null=True)
    nickname = models.CharField(max_length=16 , blank=True , null=True)
    # follower = models.ManyToManyField(User)
    # following = models.ManyToManyField(User)

    def __str__(self):
        return self.nickname
