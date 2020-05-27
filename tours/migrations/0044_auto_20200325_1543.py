# Generated by Django 2.2.3 on 2020-03-25 07:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0043_auto_20200325_1509'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TourReview',
            new_name='TourComment',
        ),
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