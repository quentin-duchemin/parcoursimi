# Generated by Django 2.0.5 on 2018-05-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcours', '0005_master_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='website',
            field=models.URLField(),
        ),
    ]
