# Generated by Django 4.1.7 on 2023-12-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='moddified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
