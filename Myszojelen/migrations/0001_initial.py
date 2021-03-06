# Generated by Django 3.0.5 on 2020-04-26 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('state_base_tax', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='State_Category_Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_val', models.FloatField(default=None)),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Category+', to='Myszojelen.Category')),
                ('id_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='State+', to='Myszojelen.State')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Category+', to='Myszojelen.Category')),
            ],
        ),
    ]
