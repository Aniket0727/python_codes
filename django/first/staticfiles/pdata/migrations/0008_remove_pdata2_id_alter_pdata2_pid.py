# Generated by Django 5.0.6 on 2024-07-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdata', '0007_alter_pdata2_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdata2',
            name='id',
        ),
        migrations.AlterField(
            model_name='pdata2',
            name='pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
