from django.db import models
from messgs.models import Campaigne


class Leads(models.Model):
    contact_number =  models.FloatField()
    name_contact = models.CharField(max_length=60, null=True)
    file_import = models.FileField(upload_to='#')
    campaigne_id = models.ForeignKey(Campaigne, on_delete=models.CASCADE)
