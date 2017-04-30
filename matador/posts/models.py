from django.db import models
import requests


class Post(models.Model):
    user = models.ForeignKey('accounts.User')
    data_post_id = models.IntegerField('post id')
    data_user_id = models.IntegerField('user id')
    title = models.TextField('title', null=True, blank=True)
    body = models.TextField('body', null=True, blank=True)

    class Meta:
        unique_together = ('user', 'data_post_id')

    @classmethod
    def get_post_for_user(cls, post_id, user):
        post = cls.objects.filter(user=user, data_post_id=post_id).first()
        if post:
            return post

        else:
            response = requests.\
                get('https://jsonplaceholder.typicode.com/posts').json()
            post = [post for post in response if post['id'] == post_id][0]
            post = Post.objects.create(data_post_id=post['id'],
                                       data_user_id=post['userId'],
                                       title=post['title'],
                                       body=post['body'],
                                       user=user)
            return post
