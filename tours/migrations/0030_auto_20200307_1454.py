# Generated by Django 2.2.3 on 2020-03-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0029_auto_20200307_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('en', 'English'), ('ko', 'Korean')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('en', 'English'), ('ko', 'Korean')], default='en', max_length=5),
        ),
    ]
