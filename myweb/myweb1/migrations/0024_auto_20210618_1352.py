# Generated by Django 2.2.2 on 2021-06-18 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb1', '0023_userprofile_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='verification',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxLengthValidator(1)]),
        ),
    ]
