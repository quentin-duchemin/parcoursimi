# Generated by Django 2.0.5 on 2018-05-24 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcours', '0002_auto_20180524_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='master',
            old_name='title',
            new_name='name',
        ),
    ]