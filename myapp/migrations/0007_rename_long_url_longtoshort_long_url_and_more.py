# Generated by Django 4.0.1 on 2022-04-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_date_longtoshort_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longtoshort',
            old_name='Long_url',
            new_name='long_url',
        ),
        migrations.RenameField(
            model_name='longtoshort',
            old_name='Short_url',
            new_name='short_url',
        ),
    ]
