# Generated by Django 4.1.3 on 2023-01-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
