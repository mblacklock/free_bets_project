# Generated by Django 2.0.7 on 2018-08-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0006_auto_20180820_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='affiliate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bets.Affiliate'),
        ),
    ]
