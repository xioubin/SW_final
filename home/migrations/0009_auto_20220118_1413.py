# Generated by Django 3.2.8 on 2022-01-18 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_info_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='last_login',
        ),
    ]
