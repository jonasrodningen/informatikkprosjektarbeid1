# Generated by Django 2.1.1 on 2018-10-20 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_remove_userlikes_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='article',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userlikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
