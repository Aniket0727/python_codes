# Generated by Django 5.0.6 on 2024-06-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdata', '0002_rename_pdata_pdata2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdata2',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='img/'),
        ),
    ]
