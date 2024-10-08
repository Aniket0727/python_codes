# Generated by Django 5.0.6 on 2024-06-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=100)),
                ('op', models.IntegerField()),
                ('sp', models.IntegerField()),
                ('pd', models.TextField()),
                ('address', models.TextField()),
                ('image', models.FileField(default=None, max_length=250, upload_to='img/')),
            ],
        ),
    ]
