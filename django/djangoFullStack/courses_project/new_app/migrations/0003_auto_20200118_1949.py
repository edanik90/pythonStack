# Generated by Django 2.2 on 2020-01-19 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20200118_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='desciption',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='new_app.Description'),
        ),
    ]