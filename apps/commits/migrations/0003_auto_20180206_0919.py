# Generated by Django 2.0.2 on 2018-02-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commits', '0002_auto_20180206_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='score_funny',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commit',
            name='score_not_funny',
            field=models.IntegerField(default=0),
        ),
    ]