# Generated by Django 2.2.3 on 2020-03-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200307_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('u', 'unidentified'), ('m', 'male'), ('f', 'female')], default='u', max_length=1),
        ),
    ]
