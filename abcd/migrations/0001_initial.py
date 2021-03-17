# Generated by Django 3.1.4 on 2021-03-17 15:35

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=127, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('assocs', models.TextField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('x_coord', models.FloatField(null=True)),
                ('y_coord', models.FloatField(null=True)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('location', models.TextField()),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=127, null=True, verbose_name='email address')),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('magnitude', models.SmallIntegerField(null=True)),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Qualities',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('magnitude', models.SmallIntegerField(null=True)),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Stakeholders',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Strengths',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('magnitude', models.SmallIntegerField(null=True)),
            ],
            bases=('abcd.node',),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abcd.node')),
                ('details', models.TextField(blank=True, null=True)),
                ('magnitude', models.SmallIntegerField(null=True)),
            ],
            bases=('abcd.node',),
        ),
    ]
