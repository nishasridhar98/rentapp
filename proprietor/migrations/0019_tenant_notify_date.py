# Generated by Django 2.1.1 on 2018-10-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proprietor', '0018_auto_20181012_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='notify_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
