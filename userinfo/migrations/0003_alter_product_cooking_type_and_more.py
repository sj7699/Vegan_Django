# Generated by Django 4.0.4 on 2022-06-08 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_product_serving_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cooking_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='primary_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='specific',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='vegan_option',
            field=models.CharField(default='', max_length=50),
        ),
    ]
