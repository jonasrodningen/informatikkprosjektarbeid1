# Generated by Django 2.1.1 on 2018-10-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_auto_20181020_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='coauthor',
        ),
    ]
