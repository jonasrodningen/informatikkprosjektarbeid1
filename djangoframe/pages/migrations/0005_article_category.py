# Generated by Django 2.1.1 on 2018-09-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180920_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]
