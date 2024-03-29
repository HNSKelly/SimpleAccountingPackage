# Generated by Django 4.1.5 on 2023-09-05 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoicing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicingFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='InvocingFile', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document Storage',
                'verbose_name_plural': 'Document Storage',
            },
        ),
        migrations.CreateModel(
            name='SalesInvoicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_types', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Invoice types')),
                ('invoicing_date', models.DateTimeField(blank=True, help_text='Automatically add on save', null=True, verbose_name='Invoicing date')),
                ('invoice_number', models.CharField(blank=True, help_text='Automatically add on save', max_length=128, null=True, unique=True, verbose_name='Invoice Number')),
                ('name_of_supplier', models.CharField(blank=True, max_length=512, null=True, verbose_name='Name of supplier')),
                ('type_of_business', models.CharField(blank=True, max_length=512, null=True, verbose_name='Type of business')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('tax_rate', models.FloatField(verbose_name='Tax rate')),
                ('total_tax', models.FloatField(blank=True, null=True, verbose_name='Total Tax')),
                ('total_price_and_tax', models.FloatField(blank=True, null=True, verbose_name='Total price and tax')),
                ('certification_status', models.CharField(blank=True, max_length=512, null=True, verbose_name='Certification Status')),
                ('date_of_certification', models.DateTimeField(blank=True, null=True, verbose_name='Date of certification')),
                ('update_time', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Update time')),
                ('creat_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SalesInvocing_creat_user', to=settings.AUTH_USER_MODEL)),
                ('invocing_file', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoicing.invoicingfile', verbose_name='Invocing File')),
                ('update_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SalesInvocing_update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InputInvoicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_types', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Invoice types')),
                ('invoicing_date', models.DateTimeField(blank=True, help_text='Automatically add on save', null=True, verbose_name='Invoicing date')),
                ('invoice_number', models.CharField(blank=True, help_text='Automatically add on save', max_length=128, null=True, unique=True, verbose_name='Invoice Number')),
                ('name_of_supplier', models.CharField(blank=True, max_length=512, null=True, verbose_name='Name of supplier')),
                ('type_of_business', models.CharField(blank=True, max_length=512, null=True, verbose_name='Type of business')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('tax_rate', models.FloatField(verbose_name='Tax rate')),
                ('total_tax', models.FloatField(blank=True, null=True, verbose_name='Total Tax')),
                ('total_price_and_tax', models.FloatField(blank=True, null=True, verbose_name='Total price and tax')),
                ('certification_status', models.CharField(blank=True, max_length=512, null=True, verbose_name='Certification Status')),
                ('date_of_certification', models.DateTimeField(blank=True, null=True, verbose_name='Date of certification')),
                ('update_time', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Update time')),
                ('creat_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='InputInvocing_creat_user', to=settings.AUTH_USER_MODEL)),
                ('invocing_file', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoicing.invoicingfile', verbose_name='Invocing File')),
                ('update_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='InputInvocing_update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
