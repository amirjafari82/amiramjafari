# Generated by Django 4.2.4 on 2023-09-07 11:02

from django.db import migrations, models
import projectreq.models


class Migration(migrations.Migration):

    dependencies = [
        ('projectreq', '0002_projectrequest_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequest',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]