# Generated by Django 4.2.4 on 2023-09-06 14:24

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0021_alter_weblog_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]
