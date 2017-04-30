from django.db import models


class Post(models.Model):
    post_id = models.IntegerField('post id')
    user_id = models.IntegerField('user id')
    title = models.TextField('title', null=True, blank=True)
    body = models.TextField('body', null=True, blank=True)


class UserPost(models.Model):
    """
    Through many to many model for extra customization.
    """
    user_id = models.ForeignKey('accounts.User')
    post_id = models.ForeignKey(Post)
