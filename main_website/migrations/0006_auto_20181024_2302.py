# Generated by Django 2.1 on 2018-10-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0005_auto_20181024_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
