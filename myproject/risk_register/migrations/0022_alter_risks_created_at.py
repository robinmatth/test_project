# Generated by Django 4.0.1 on 2022-02-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0021_risks_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risks',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
