# Generated by Django 4.2.5 on 2023-10-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
