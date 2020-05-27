# Generated by Django 2.2.3 on 2020-03-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200323_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('u', 'unidentified'), ('f', 'female')], default='u', max_length=1),
        ),
    ]
