# Generated by Django 2.1.1 on 2018-10-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proprietor', '0012_auto_20181001_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='rent_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]