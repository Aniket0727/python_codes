# Generated by Django 5.0.6 on 2024-06-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0003_rename_mydata2_mydata3'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=100)),
                ('op', models.IntegerField(max_length=100)),
                ('sp', models.IntegerField(max_length=100)),
                ('pd', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('image', models.FileField(default=None, max_length=250, upload_to='img/')),
            ],
        ),
    ]
