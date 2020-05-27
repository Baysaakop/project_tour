# Generated by Django 2.2.3 on 2020-03-23 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0037_auto_20200323_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='itinerary',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='price',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Tour'),
        ),
        migrations.AddField(
            model_name='price',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Tour'),
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