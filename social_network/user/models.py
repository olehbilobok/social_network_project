from django.db import models
from django.contrib.auth.models import User


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user: {self.user}, action: {self.action}, timestamp: {self.timestamp}"

    # def __repr__(self):
    #     return f"{self.__class__.__name__}(id={self.id})"