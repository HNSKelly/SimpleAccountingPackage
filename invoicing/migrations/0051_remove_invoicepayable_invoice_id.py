# Generated by Django 4.1.5 on 2023-10-24 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0050_invoicepayable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicepayable',
            name='invoice_id',
        ),
    ]
