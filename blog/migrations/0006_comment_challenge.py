# Generated by Django 5.0.2 on 2024-03-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default=''),
        ),
    ]
