# Generated by Django 4.1.5 on 2023-10-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0023_alter_invoice_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
