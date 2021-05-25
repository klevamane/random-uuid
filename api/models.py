from django.db import models


class RandomUid(models.Model):
    uuid = models.UUIDField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

