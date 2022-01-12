# Generated by Django 4.0 on 2022-01-08 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
            bases=('core.defaultobject', models.Model),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
            },
            bases=('core.defaultobject', models.Model),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
                ('floor', models.IntegerField(verbose_name='floor')),
                ('department_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.department', verbose_name='department')),
            ],
            options={
                'verbose_name': 'map',
                'verbose_name_plural': 'maps',
            },
            bases=('core.defaultobject', models.Model),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('defaultobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.defaultobject')),
                ('x', models.IntegerField(verbose_name='x')),
                ('y', models.IntegerField(verbose_name='y')),
                ('area_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.area', verbose_name='area')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
            bases=('core.defaultobject', models.Model),
        ),
    ]
