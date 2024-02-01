# Generated by Django 4.1.13 on 2024-02-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_comment_comment_add_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_text',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
