# Generated by Django 4.0.1 on 2022-01-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0003_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risks',
            name='risk_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='risks',
            name='risk_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
