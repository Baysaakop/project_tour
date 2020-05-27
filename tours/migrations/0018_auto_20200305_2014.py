# Generated by Django 3.0.3 on 2020-03-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0017_auto_20200305_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('¥', 'JPY'), ('₩', 'KRW')], default='$', max_length=5),
        ),
    ]
