# Generated by Django 4.2 on 2023-04-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
