# Generated by Django 3.2.8 on 2022-03-01 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtravelapp', '0002_auto_20220301_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdb',
            old_name='Phone',
            new_name='Phonenumber',
        ),
        migrations.RemoveField(
            model_name='registerdb',
            name='mobile',
        ),
    ]
