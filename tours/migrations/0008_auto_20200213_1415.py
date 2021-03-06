# Generated by Django 2.2.3 on 2020-02-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_auto_20200213_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='currency',
            field=models.CharField(choices=[('¥', 'JPY'), ('$', 'USD'), ('₩', 'KRW'), ('元', 'RMB')], default='$', max_length=2),
        ),
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('ko', 'Korean'), ('zh-cn', 'Chinese'), ('en', 'English')], default='en', max_length=2),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('ko', 'Korean'), ('zh-cn', 'Chinese'), ('en', 'English')], default='en', max_length=2),
        ),
    ]
