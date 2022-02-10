# Generated by Django 4.0.1 on 2022-02-07 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0015_alter_risks_risk_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='risks',
        ),
        migrations.AddField(
            model_name='projects',
            name='risks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='risk_register.risks'),
        ),
    ]