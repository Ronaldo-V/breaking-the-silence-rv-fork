# Generated by Django 4.2 on 2023-04-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0002_rename_request_connectionrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionrequest',
            name='dismissed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name='connectionrequest',
            constraint=models.UniqueConstraint(fields=('sender', 'receiver'), name='unique_match'),
        ),
    ]
