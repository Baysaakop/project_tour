# Generated by Django 2.2.3 on 2020-03-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0028_auto_20200307_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourreview',
            old_name='review',
            new_name='comment',
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
