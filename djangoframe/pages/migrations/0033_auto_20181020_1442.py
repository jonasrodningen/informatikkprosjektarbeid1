# Generated by Django 2.1.1 on 2018-10-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20181020_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlikes',
            name='user',
        ),
        migrations.AddField(
            model_name='userlikes',
            name='userid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userlikes',
            name='articleid',
            field=models.IntegerField(default=0),
        ),
    ]
