# Generated by Django 2.2.3 on 2020-03-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200323_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('u', 'unidentified')], default='u', max_length=1),
        ),
    ]