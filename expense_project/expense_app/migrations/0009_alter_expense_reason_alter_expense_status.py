# Generated by Django 4.0.1 on 2022-01-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0008_rename_expenses_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='reason',
            field=models.CharField(choices=[('FO', 'Food'), ('MI', 'Mileage'), ('EQ', 'Equipment'), ('OT', 'Other')], default='OT', max_length=2),
        ),
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.CharField(choices=[('AP', 'Approved'), ('RE', 'Rejected'), ('DR', 'Draft'), ('PE', 'Pending')], default='PE', max_length=2),
        ),
    ]
