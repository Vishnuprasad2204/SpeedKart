# Generated by Django 4.2.16 on 2024-12-27 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0011_product_table_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpeedKartApp.usertable_model'),
        ),
    ]
