# Generated by Django 3.0.2 on 2020-05-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20200503_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
