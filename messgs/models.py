from django.db import models
from accounts.models import Account


class Campaigne(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    number_telephone = models.CharField(max_length=30, null=False)

class Message(models.Model):
    JPG = 'JPG'
    PNG = 'PNG'
    AUD = 'AUD'
    VID = 'VID'
    TXT = 'TXT'

    types_accepted = [
        (JPG, 'JPG'),
        (PNG, 'PNG'),
        (AUD, 'AUDIO'),
        (VID, 'VIDEO'),
        (TXT, 'TXT'),
    ]
    type_mime = models.CharField(
        max_length=3,
        choices=types_accepted,
        default=TXT
    )
    content_image = models.ImageField(upload_to="#", null=True)

    # content_audio= models.AudioField(===, null=True)
