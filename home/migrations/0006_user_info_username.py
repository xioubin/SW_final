# Generated by Django 3.2.8 on 2022-01-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_user_info_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
