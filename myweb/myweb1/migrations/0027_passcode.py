# Generated by Django 2.2.2 on 2021-06-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb1', '0026_auto_20210619_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='passcode',
            fields=[
                ('idno', models.BigAutoField(primary_key=True, serialize=False)),
                ('pin', models.CharField(max_length=7)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]