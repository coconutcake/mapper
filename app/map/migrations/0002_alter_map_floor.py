# Generated by Django 4.0 on 2022-01-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='floor',
            field=models.IntegerField(verbose_name='floor'),
        ),
    ]