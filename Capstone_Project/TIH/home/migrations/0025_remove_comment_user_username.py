# Generated by Django 4.1.13 on 2024-02-02 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_comment_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_username',
        ),
    ]
