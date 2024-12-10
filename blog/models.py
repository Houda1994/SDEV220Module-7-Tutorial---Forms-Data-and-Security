from django.db import models
# we afre going to use some package to help us
# this will help us add this model to the admin panel later
from django.conf import settings
# import functions to deal with timestamps and timezones
from django.utils import timezone


# create your models here.

# let's make our post table


class Post(models.Model):
    # this is a foreign key to the user table
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # this is the title of the post
    title = models.CharField(max_length=200)
    # this is the content of the post
    text = models.TextField()
    # this is the date the post was created
    created_date = models.DateTimeField(default=timezone.now)
    # this is the date the post was published
    published_date = models.DateTimeField(blank=True, null=True)

    # this function will publish the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()  # django way to save to a database

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text