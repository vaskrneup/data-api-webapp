# Generated by Django 3.0.4 on 2020-03-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareManager', '0004_sharemanagerusersharevalues_share_company_buy_or_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharemanagerusersharevalues',
            name='share_company_bought_remarks',
            field=models.TextField(blank=True, default='Null'),
        ),
    ]
