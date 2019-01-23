# Generated by Django 2.1.5 on 2019-01-18 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecwc_sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=10)),
                ('user_id', models.PositiveIntegerField()),
                ('session_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecwc_sessions.Session_Model')),
            ],
        ),
    ]
