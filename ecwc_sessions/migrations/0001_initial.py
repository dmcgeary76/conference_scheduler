# Generated by Django 2.1.5 on 2019-01-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presenter', models.CharField(max_length=120)),
                ('org', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=500)),
                ('domain', models.CharField(max_length=120)),
                ('age_range', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=120)),
                ('room', models.CharField(max_length=120)),
                ('time_slot', models.CharField(max_length=120)),
                ('room_limit', models.PositiveIntegerField()),
            ],
        ),
    ]
