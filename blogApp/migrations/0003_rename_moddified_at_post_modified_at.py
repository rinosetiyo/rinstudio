# Generated by Django 4.1.7 on 2023-12-15 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_post_created_at_post_moddified_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='moddified_at',
            new_name='modified_at',
        ),
    ]
