# Generated by Django 3.0.3 on 2020-03-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0016_auto_20200301_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('₩', 'KRW'), ('¥', 'JPY')], default='$', max_length=5),
        ),
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('ko', 'Korean'), ('en', 'English')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('ko', 'Korean'), ('en', 'English')], default='en', max_length=5),
        ),
    ]
