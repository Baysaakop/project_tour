# Generated by Django 2.2.3 on 2020-05-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200527_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('u', 'unidentified'), ('f', 'female')], default='u', max_length=1),
        ),
    ]
