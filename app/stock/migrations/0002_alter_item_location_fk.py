# Generated by Django 4.0 on 2022-01-08 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_equipment', '0007_locationtype_location'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_equipment.location', verbose_name='location'),
        ),
    ]
