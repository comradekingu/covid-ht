# Generated by Django 3.1.5 on 2021-01-11 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('timezone', models.CharField(default='America/Lima', max_length=100, verbose_name='Time zone')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
    ]
