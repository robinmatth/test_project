# Generated by Django 4.0.1 on 2022-02-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0019_delete_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='risks',
            name='risks_id',
            field=models.IntegerField(default=0),
        ),
    ]