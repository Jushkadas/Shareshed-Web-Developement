# Generated by Django 2.1 on 2018-10-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0002_user_has_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='has_verified',
            field=models.BooleanField(default=False, help_text='Member has been verified at the shed'),
        ),
    ]
