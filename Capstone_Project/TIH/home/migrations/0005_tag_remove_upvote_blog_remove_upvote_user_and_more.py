# Generated by Django 4.1.13 on 2024-01-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_blog_uid_upvote_comment_blog_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
