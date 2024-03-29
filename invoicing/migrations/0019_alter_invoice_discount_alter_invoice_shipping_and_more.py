# Generated by Django 4.1.5 on 2023-09-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0018_alter_invoice_discount_alter_invoice_shipping_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
