# Generated by Django 3.1.5 on 2021-03-24 23:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_data_alter_is_covid19'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
