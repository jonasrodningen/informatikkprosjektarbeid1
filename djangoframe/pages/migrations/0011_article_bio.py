# Generated by Django 2.1.1 on 2018-09-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
