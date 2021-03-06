# Generated by Django 3.2.8 on 2022-01-20 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='is_superadmin')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ErrorReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.IntegerField(choices=[(0, 'ROOM 1'), (1, 'ROOM 2'), (2, 'ROOM 3'), (3, 'ROOM 4'), (4, 'ROOM 5')])),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('time', models.IntegerField(choices=[(0, '8-9'), (1, '9-10'), (2, '10-11'), (3, '11-12'), (4, '12-13'), (5, '13-14'), (1, '14-15'), (2, '16-17')])),
                ('invitees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
