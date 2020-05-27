# Generated by Django 3.0.3 on 2020-03-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0038_auto_20200323_1521'),
    ]

    operations = [
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