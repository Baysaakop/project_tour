# Generated by Django 2.2.3 on 2020-03-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0035_auto_20200323_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='currency',
            field=models.CharField(choices=[('¥', 'JPY'), ('₩', 'KRW'), ('$', 'USD')], default='$', max_length=5),
        ),
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ko', 'Korean'), ('ja', 'Japanese'), ('en', 'English')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ko', 'Korean'), ('ja', 'Japanese'), ('en', 'English')], default='en', max_length=5),
        ),
    ]
