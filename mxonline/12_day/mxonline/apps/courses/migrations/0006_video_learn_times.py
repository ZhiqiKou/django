# Generated by Django 2.0.3 on 2018-08-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='学习时长(分钟)'),
        ),
    ]
