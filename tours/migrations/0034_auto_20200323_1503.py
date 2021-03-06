# Generated by Django 2.2.3 on 2020-03-23 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0033_auto_20200323_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourreview',
            name='is_liked',
        ),
        migrations.AddField(
            model_name='tourreview',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tour',
            name='currency',
            field=models.CharField(choices=[('₩', 'KRW'), ('$', 'USD'), ('¥', 'JPY')], default='$', max_length=5),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='tours.TourImage'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('en', 'English'), ('ko', 'Korean')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='tourreview',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour'),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ja', 'Japanese'), ('en', 'English'), ('ko', 'Korean')], default='en', max_length=5),
        ),
    ]
