# Generated by Django 4.0.1 on 2022-01-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0010_remove_projects_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_description',
            field=models.CharField(default=0, max_length=300),
        ),
    ]