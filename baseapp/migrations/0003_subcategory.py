# Generated by Django 4.1.3 on 2022-12-31 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubCategory', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.category')),
            ],
        ),
    ]
