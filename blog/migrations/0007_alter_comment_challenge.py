# Generated by Django 5.0.2 on 2024-03-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default='3.0'),
        ),
    ]
