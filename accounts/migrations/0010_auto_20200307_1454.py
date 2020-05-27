# Generated by Django 2.2.3 on 2020-03-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200307_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male'), ('u', 'unidentified')], default='u', max_length=1),
        ),
    ]