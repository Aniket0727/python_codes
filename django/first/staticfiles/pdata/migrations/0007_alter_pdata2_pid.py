# Generated by Django 5.0.6 on 2024-07-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdata', '0006_pdata2_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdata2',
            name='pid',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
