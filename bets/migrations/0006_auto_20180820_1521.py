# Generated by Django 2.0.7 on 2018-08-20 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bets', '0005_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='affiliate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Affiliate'),
        ),
        migrations.AddField(
            model_name='click',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='click',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
