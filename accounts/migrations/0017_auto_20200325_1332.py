# Generated by Django 2.2.3 on 2020-03-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200324_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male'), ('u', 'unidentified')], default='u', max_length=1),
        ),
    ]
