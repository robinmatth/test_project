# Generated by Django 4.0.1 on 2022-02-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_register', '0022_alter_risks_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.CharField(max_length=200)),
                ('risks', models.ManyToManyField(to='risk_register.Risks')),
            ],
            options={
                'verbose_name': 'Projects',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
