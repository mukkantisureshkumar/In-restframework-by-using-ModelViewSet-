# Generated by Django 5.0.6 on 2024-07-09 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('categoryname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('categoryid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Pname', models.CharField(max_length=100)),
                ('Pid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
    ]