# Generated by Django 2.2.6 on 2020-01-29 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
