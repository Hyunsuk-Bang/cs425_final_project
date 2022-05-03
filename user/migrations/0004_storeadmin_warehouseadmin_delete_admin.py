# Generated by Django 4.0.4 on 2022-05-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='storeAdmin',
            fields=[
                ('store_a_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'storeAdmin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='warehouseAdmin',
            fields=[
                ('wh_a_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'warehouseAdmin',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
