# Generated by Django 2.2.2 on 2021-06-13 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myweb1', '0008_post_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myweb1.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb1.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]