# Generated by Django 4.0.1 on 2022-01-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0006_alter_risks_risk_impact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risks',
            name='risk_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='risks',
            name='risk_due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
