# Generated by Django 2.2 on 2021-10-22 16:58

import SuiteApp.utils
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('SuiteApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblRol',
            fields=[
                ('rol', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='registrarUsuario',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.TextField(max_length=150)),
                ('telefono_particular', models.CharField(max_length=10, validators=[SuiteApp.utils.validate_only_numbers])),
                ('telefono_celular', models.CharField(max_length=8, validators=[SuiteApp.utils.validate_only_numbers])),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuiteApp.tblRol')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
