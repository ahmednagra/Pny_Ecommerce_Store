# Generated by Django 4.1.4 on 2023-01-31 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0010_rename_category_name_category_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 22, 1, 56, 26178)),
        ),
    ]