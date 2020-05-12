# Generated by Django 3.0.2 on 2020-05-03 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0004_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_actions', to=settings.AUTH_USER_MODEL),
        ),
    ]
