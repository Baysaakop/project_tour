# Generated by Django 2.2.3 on 2020-03-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200307_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('u', 'unidentified'), ('m', 'male')], default='u', max_length=1),
        ),
    ]
