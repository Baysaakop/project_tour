# Generated by Django 2.2.3 on 2020-03-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200306_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('u', 'unidentified'), ('m', 'male')], default='u', max_length=1),
        ),
    ]
