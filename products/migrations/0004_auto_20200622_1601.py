# Generated by Django 3.0.6 on 2020-06-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.PositiveSmallIntegerField(default=2010, null=True, verbose_name='Дата выхода на рынок'),
        ),
    ]
