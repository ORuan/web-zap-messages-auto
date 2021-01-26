from django.db import models
from messgs.models import Campaigne


class Leads(models.Model):
    contact_number =  models.FloatField()
    campaigne_id = models.ForeignKey(Campaigne, on_delete=models.CASCADE)