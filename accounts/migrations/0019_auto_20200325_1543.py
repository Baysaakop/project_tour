# Generated by Django 2.2.3 on 2020-03-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200325_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('u', 'unidentified'), ('f', 'female')], default='u', max_length=1),
        ),
    ]
