# Generated by Django 4.1.13 on 2024-02-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_remove_blog_dummy_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=5000),
        ),
    ]
