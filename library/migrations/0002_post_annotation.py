# Generated by Django 3.2.16 on 2022-12-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='annotation',
            field=models.TextField(default=''),
        ),
    ]
