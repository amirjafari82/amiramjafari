# Generated by Django 4.2.4 on 2023-09-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('phone', models.CharField(max_length=11)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
