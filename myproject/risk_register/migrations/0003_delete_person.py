# Generated by Django 4.0.1 on 2022-01-15 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0002_person_delete_impact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
