# Generated by Django 2.2.2 on 2021-06-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb1', '0025_auto_20210618_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='idno',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='idno',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='slno',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='idno',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]