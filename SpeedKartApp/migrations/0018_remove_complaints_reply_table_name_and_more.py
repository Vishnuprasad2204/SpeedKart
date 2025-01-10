# Generated by Django 4.2.16 on 2025-01-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0017_productrate_table_complaint_productrate_table_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints_reply_table',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='review_table',
            name='Name',
        ),
        migrations.AddField(
            model_name='complaints_reply_table',
            name='SELLER_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpeedKartApp.seller_table'),
        ),
        migrations.DeleteModel(
            name='ShopTable_model',
        ),
    ]
