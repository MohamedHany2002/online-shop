# Generated by Django 3.0.2 on 2020-05-03 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('analytics', '0006_auto_20200503_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='contentType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
