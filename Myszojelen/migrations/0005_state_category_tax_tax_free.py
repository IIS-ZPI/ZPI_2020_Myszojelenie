# Generated by Django 3.0.5 on 2020-05-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myszojelen', '0004_auto_20200426_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='state_category_tax',
            name='tax_free',
            field=models.FloatField(default=0),
        ),
    ]
