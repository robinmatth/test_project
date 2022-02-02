# Generated by Django 4.0.1 on 2022-01-31 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0011_projects_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project',
        ),
        migrations.AddField(
            model_name='projects',
            name='risks',
            field=models.ManyToManyField(blank=True, to='risk_register.Risks'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_description',
            field=models.CharField(max_length=200),
        ),
    ]