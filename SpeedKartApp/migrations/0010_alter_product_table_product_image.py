# Generated by Django 4.2.16 on 2024-12-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0009_complaints_reply_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='Product_image',
            field=models.FileField(blank=True, null=True, upload_to='product/'),
        ),
    ]
