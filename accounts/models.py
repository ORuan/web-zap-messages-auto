from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Account(models.Model):
    active = models.BooleanField(default=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=timezone.now(), editable=False)
    edited_at = models.DateTimeField(auto_now=timezone.now())


class Tokens(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4)
    time_expires = models.TimeField(null=False)
    update_at = models.DateTimeField(auto_now_add=timezone.now())