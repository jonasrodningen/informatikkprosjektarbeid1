# Generated by Django 2.1.1 on 2018-09-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]
