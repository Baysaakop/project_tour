# Generated by Django 2.2.3 on 2020-03-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200306_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('u', 'unidentified'), ('f', 'female')], default='u', max_length=1),
        ),
    ]
