# Generated by Django 4.0 on 2022-02-04 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_somemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebook',
            old_name='digional',
            new_name='diagonal',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='display',
            new_name='display_type',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='digional',
            new_name='diagonal',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='display',
            new_name='display_type',
        ),
    ]
