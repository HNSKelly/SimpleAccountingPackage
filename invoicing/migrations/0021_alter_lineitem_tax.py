# Generated by Django 4.1.5 on 2023-10-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0020_alter_invoice_total_amount_alter_lineitem_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='tax',
            field=models.FloatField(default=0.1, verbose_name='Tax'),
        ),
    ]