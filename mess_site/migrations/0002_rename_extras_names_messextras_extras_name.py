# Generated by Django 4.1.2 on 2022-12-24 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messextras',
            old_name='extras_names',
            new_name='extras_name',
        ),
    ]
