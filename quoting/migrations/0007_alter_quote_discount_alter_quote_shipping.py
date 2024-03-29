# Generated by Django 4.1.5 on 2023-10-16 04:56

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoting', '0006_quote_status_alter_lineitem_tax_alter_quote_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
    ]
