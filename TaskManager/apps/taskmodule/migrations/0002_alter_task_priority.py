# Generated by Django 5.0.6 on 2024-05-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=6),
        ),
    ]
