# Generated by Django 3.0.4 on 2020-05-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareManager', '0014_auto_20200507_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
            ],
        ),
    ]