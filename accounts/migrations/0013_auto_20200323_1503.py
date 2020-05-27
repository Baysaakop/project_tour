# Generated by Django 2.2.3 on 2020-03-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200323_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('u', 'unidentified'), ('m', 'male'), ('f', 'female')], default='u', max_length=1),
        ),
    ]