from django.db import models
from django.conf import settings
import pytz
from django.utils import timezone

class Post(models.Model):
    """ The Posts Models """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='posts', blank=True)
    text = models.TextField(max_length=2048, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s post"

    @property
    def posted_date_ist(self):
        # Convert UTC to IST
        return self.posted_date.astimezone(pytz.timezone('Asia/Kolkata'))

class Comment(models.Model):
    """ The comments Models """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=2048, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    @property
    def comment_date_ist(self):
        # Convert UTC to IST
        return self.comment_date.astimezone(pytz.timezone('Asia/Kolkata'))
