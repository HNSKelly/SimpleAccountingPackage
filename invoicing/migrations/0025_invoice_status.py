# Generated by Django 4.1.5 on 2023-10-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0024_alter_invoice_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('UNPAID', 'Unpaid')], default='UNPAID', max_length=10),
        ),
    ]