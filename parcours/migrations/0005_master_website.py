# Generated by Django 2.0.5 on 2018-05-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcours', '0004_auto_20180524_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]