# Generated by Django 3.1 on 2021-01-18 19:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210118_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 1, 18, 19, 52, 20, 134486, tzinfo=utc), editable=False),
        ),
    ]
