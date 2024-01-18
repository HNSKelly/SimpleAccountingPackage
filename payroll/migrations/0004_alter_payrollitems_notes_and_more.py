# Generated by Django 4.1.5 on 2023-09-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_alter_payroll_total_wages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrollitems',
            name='notes',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Payroll notes'),
        ),
        migrations.AlterField(
            model_name='payrollitems',
            name='wage_items',
            field=models.CharField(max_length=128, verbose_name='Wage items'),
        ),
    ]
