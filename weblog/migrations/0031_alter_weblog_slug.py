# Generated by Django 4.2.4 on 2023-09-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0030_alter_weblog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
