# Generated by Django 4.2.4 on 2023-09-09 13:44

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0023_alter_weblog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='image',
            field=models.ImageField(upload_to=pathlib.PurePosixPath('/home/amiramj1/CVWebsite/static/images/weblog')),
        ),
    ]