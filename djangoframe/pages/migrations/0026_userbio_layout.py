# Generated by Django 2.1.1 on 2018-10-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20181019_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbio',
            name='layout',
            field=models.IntegerField(default=1),
        ),
    ]
