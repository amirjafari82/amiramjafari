# Generated by Django 4.2.4 on 2023-09-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0003_weblog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]
