# Generated by Django 2.1.1 on 2018-10-20 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_auto_20181020_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlikes',
            old_name='article',
            new_name='articleid',
        ),
    ]
