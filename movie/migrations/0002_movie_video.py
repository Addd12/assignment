# Generated by Django 3.1.7 on 2021-04-19 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.CharField(default='https://www.youtube.com/watch?v=u22BXhMu4tI', max_length=200),
            preserve_default=False,
        ),
    ]
