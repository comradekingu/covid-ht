# Generated by Django 3.2.8 on 2021-10-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_example_data_v2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
