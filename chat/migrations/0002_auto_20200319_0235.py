# Generated by Django 3.0.4 on 2020-03-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.SlugField(max_length=120),
        ),
    ]
