# Generated by Django 4.0.3 on 2022-04-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
    ]