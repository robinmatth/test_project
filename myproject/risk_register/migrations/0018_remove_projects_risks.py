# Generated by Django 4.0.1 on 2022-02-07 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0017_alter_projects_risks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='risks',
        ),
    ]
