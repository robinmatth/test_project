# Generated by Django 4.0.1 on 2022-01-31 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0009_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
    ]
