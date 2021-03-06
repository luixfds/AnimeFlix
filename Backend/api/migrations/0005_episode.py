# Generated by Django 4.0.3 on 2022-04-16 02:02

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_epsgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('animename', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to=api.models.episode_file)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.epsgroup')),
            ],
        ),
    ]
