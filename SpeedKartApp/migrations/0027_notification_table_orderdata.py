# Generated by Django 4.2.16 on 2025-01-19 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0026_rename_order_name_notification_table_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_table',
            name='orderdata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpeedKartApp.order_table'),
        ),
    ]
