# Generated by Django 5.1.6 on 2025-03-06 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
