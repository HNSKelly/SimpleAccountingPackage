# Generated by Django 4.1.5 on 2023-09-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0005_client_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='aus_business_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ABN'),
        ),
    ]
