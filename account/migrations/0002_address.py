# Generated by Django 3.0.2 on 2020-04-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=120)),
                ('address_line', models.CharField(max_length=120)),
                ('address_line2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
            ],
        ),
    ]
