# Generated by Django 2.1.5 on 2019-01-20 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecwc_sessions', '0003_auto_20190119_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_model',
            name='seats',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
