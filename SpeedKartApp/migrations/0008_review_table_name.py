# Generated by Django 4.2.16 on 2024-12-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpeedKartApp', '0007_remove_review_table_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_table',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
