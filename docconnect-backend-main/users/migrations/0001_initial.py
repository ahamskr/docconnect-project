# Generated by Django 4.1.3 on 2022-11-19 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'is_superadmin'), (2, 'is_admin'), (3, 'is_job_seeker'), (4, 'is_organisation')], primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, choices=[('IS_SUPERADMIN', 'is_superadmin'), ('IS_ADMIN', 'is_admin'), ('IS_JOB_SEEKER', 'is_job_seeker'), ('IS_ORGANISATION', 'is_organisation')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('roles', models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
