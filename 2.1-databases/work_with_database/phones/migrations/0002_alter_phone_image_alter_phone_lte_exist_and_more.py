# Generated by Django 4.1.4 on 2022-12-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exist',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(max_length=15),
        ),
    ]