# Generated by Django 4.2.4 on 2023-09-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_weblog_body_weblog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblog',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]