# Generated by Django 4.2.16 on 2025-01-11 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0021_request_table_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints_reply_table',
            name='DELIVERY',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpeedKartApp.delivery_agent_table'),
        ),
    ]
