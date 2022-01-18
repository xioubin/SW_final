# Generated by Django 3.2.8 on 2022-01-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_user_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='username',
        ),
        migrations.AddField(
            model_name='user_info',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
