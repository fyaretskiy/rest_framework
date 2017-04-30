from django.db import models


class Posts(models.Model):
    post_id = models.IntegerField('post id')
    user_id = models.IntegerField('user id')
    title = models.TextField('title', null=True, blank=True)
    body = models.TextField('body', null=True, blank=True)

