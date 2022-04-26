# Generated by Django 4.0.4 on 2022-04-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('s_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('w_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'warehouse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Storeinv',
            fields=[
                ('s', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.store')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'storeINV',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Storereorder',
            fields=[
                ('s', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.store')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('reorderdate', models.DateField(db_column='reorderDate')),
            ],
            options={
                'db_table': 'storeReorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warehouseinv',
            fields=[
                ('w', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.warehouse')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'warehouseINV',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warehousereorder',
            fields=[
                ('w', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.warehouse')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('reorderdate', models.DateField(db_column='reorderDate')),
            ],
            options={
                'db_table': 'warehouseReorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Whcoverage',
            fields=[
                ('w', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.warehouse')),
                ('state', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'whCoverage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Whstore',
            fields=[
                ('w', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='warehouseStore.warehouse')),
            ],
            options={
                'db_table': 'whStore',
                'managed': False,
            },
        ),
    ]