from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    # post_comment : reverse call
    
    created_by = models.ForeignKey(User , on_delete=models.CASCADE , related_name='userpost')
    description = models.CharField(max_length=150 , null=True , blank=True)
    media_link = models.CharField(max_length=200 , null=True , blank=True)
    # reacted_by = models.ManyToManyField(User)
    # shared_by = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_by} posted "{self.description}" {self.created_at}'

class PostComment(models.Model):
    created_by = models.ForeignKey(User , on_delete=models.CASCADE , default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=230)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='post_comment')

    def __str__(self):
        return f'{self.created_by} commendted "{self.comment}" on {self.post}'

