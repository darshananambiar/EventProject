# Generated by Django 4.2 on 2025-03-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
