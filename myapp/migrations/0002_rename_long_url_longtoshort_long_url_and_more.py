# Generated by Django 4.0.1 on 2022-04-07 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longtoshort',
            old_name='long_url',
            new_name='Long_Url',
        ),
        migrations.RenameField(
            model_name='longtoshort',
            old_name='short_url',
            new_name='Short_Url',
        ),
    ]
