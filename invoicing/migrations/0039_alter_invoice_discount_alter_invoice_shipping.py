# Generated by Django 4.1.5 on 2023-10-10 00:54

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0038_alter_invoice_discount_alter_invoice_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
