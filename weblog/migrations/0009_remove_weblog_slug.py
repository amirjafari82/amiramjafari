# Generated by Django 4.2.4 on 2023-09-05 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0008_alter_weblog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblog',
            name='slug',
        ),
    ]
