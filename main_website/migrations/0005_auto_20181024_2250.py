# Generated by Django 2.1 on 2018-10-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0004_auto_20181024_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='maillist',
            field=models.BooleanField(default=True, help_text='Member subscribed to mail list'),
        ),
    ]