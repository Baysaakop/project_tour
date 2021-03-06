# Generated by Django 2.2.3 on 2020-03-06 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0022_auto_20200306_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='language',
            field=models.CharField(choices=[('ko', 'Korean'), ('ja', 'Japanese'), ('en', 'English')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='tour',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tour',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tourtype',
            name='language',
            field=models.CharField(choices=[('ko', 'Korean'), ('ja', 'Japanese'), ('en', 'English')], default='en', max_length=5),
        ),
        migrations.CreateModel(
            name='TourReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
