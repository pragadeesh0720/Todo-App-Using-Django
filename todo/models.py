from django.db import models
from django.contrib.auth.models import User

# Create your models here. - database structure


class Task(models.Model):
    # create attributes
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # on delete tells that what we do with the user when his acc is deleted so be his tasks
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = "user"
