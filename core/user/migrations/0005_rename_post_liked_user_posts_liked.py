# Generated by Django 4.0 on 2023-09-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0004_user_post_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='post_liked',
            new_name='posts_liked',
        ),
    ]