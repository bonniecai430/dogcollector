# Generated by Django 4.0.4 on 2022-07-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_sport_alter_bid_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='sports',
            field=models.ManyToManyField(to='main_app.sport'),
        ),
    ]
