# Generated by Django 4.0.1 on 2022-04-07 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_long_url_longtoshort_long_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longtoshort',
            old_name='Long_Url',
            new_name='long_url',
        ),
        migrations.RenameField(
            model_name='longtoshort',
            old_name='Short_Url',
            new_name='short_url',
        ),
    ]