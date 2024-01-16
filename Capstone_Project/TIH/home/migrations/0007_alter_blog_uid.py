# Generated by Django 4.1.13 on 2024-01-16 10:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_blog_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
