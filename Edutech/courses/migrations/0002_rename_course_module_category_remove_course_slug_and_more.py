# Generated by Django 4.2.5 on 2023-10-04 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='course',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='module',
            name='slug',
        ),
    ]
