from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Tokens(models.Model):
    token = models.UUIDField(default=uuid.uuid4)
    time_expires = models.TimeField(null=False)
    update_at = models.DateTimeField(auto_now_add=timezone.now())

class Account(models.Model):
    active = models.BooleanField(default=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=timezone.now(), editable=False)
    edited_at = models.DateTimeField(auto_now=timezone.now())
    tokens_id = models.ForeignKey(Tokens, on_delete=models.CASCADE)
    #mudar esse workspace
    has_workspace = models.BooleanField(default=False)
    path_workspace = models.CharField(max_length=255, null=True)
