# Generated by Django 4.2.4 on 2023-09-05 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0013_remove_weblog_p2_remove_weblog_p3_remove_weblog_p4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblog',
            name='p1',
        ),
    ]