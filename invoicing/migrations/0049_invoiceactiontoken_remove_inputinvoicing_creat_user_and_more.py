# Generated by Django 4.1.5 on 2023-10-24 05:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0048_alter_invoice_discount_alter_invoice_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceActionToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicing.invoice')),
            ],
        ),
        migrations.RemoveField(
            model_name='inputinvoicing',
            name='creat_user',
        ),
        migrations.RemoveField(
            model_name='inputinvoicing',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='inputinvoicing',
            name='update_user',
        ),
        migrations.DeleteModel(
            name='InvoicingFile',
        ),
        migrations.RemoveField(
            model_name='salesinvoicing',
            name='client',
        ),
        migrations.RemoveField(
            model_name='salesinvoicing',
            name='creat_user',
        ),
        migrations.RemoveField(
            model_name='salesinvoicing',
            name='update_user',
        ),
        migrations.DeleteModel(
            name='InputInvoicing',
        ),
        migrations.DeleteModel(
            name='SalesInvoicing',
        ),
    ]
