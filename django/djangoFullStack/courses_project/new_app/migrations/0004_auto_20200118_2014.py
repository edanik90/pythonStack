# Generated by Django 2.2 on 2020-01-19 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_auto_20200118_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='desciption',
            new_name='description',
        ),
    ]
