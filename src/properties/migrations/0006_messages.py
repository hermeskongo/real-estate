# Generated by Django 5.1.6 on 2025-03-05 20:10

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_properties_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[("Programmation d'une visite", "Programmation d'une visite"), ("Plus d'information", "Plus d'information"), ('Réservation du bien', 'Réservation du bien')], max_length=50, verbose_name='Sujet du message')),
                ('firstname', models.CharField(blank=True, max_length=75, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=50, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('content', models.TextField(blank=True, verbose_name='Contenu')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, error_messages={'invalid': 'Veuillez entrez un numéro de téléphone valide'}, max_length=128, null=True, region=None, unique=True)),
                ('properties', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Messagess',
            },
        ),
    ]
