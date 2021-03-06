# Generated by Django 4.0.3 on 2022-04-16 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_anime'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.anime')),
            ],
        ),
    ]
