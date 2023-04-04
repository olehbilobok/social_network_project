import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"title: {self.title}, user: {self.user}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title})"

    @property
    def likes_count(self):
        return self.likes.count()


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=datetime.datetime.now())

    def __str__(self):
        return f"user: {self.user}, {self.post}, created_at: {self.created_at}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
