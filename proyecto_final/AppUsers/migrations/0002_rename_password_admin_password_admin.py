# Generated by Django 4.2.6 on 2023-10-22 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='password',
            new_name='password_admin',
        ),
    ]
