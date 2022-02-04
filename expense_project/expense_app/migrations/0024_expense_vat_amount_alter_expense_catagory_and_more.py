# Generated by Django 4.0.1 on 2022-02-02 23:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0023_expense_persons_seen_alter_expense_catagory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='VAT_amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='expense',
            name='catagory',
            field=models.CharField(choices=[('AC', 'Accommodation'), ('CE', 'Client entertainment (Incl VAT)'), ('FL', 'Flights'), ('MI', 'Mileage'), ('OT', 'Other'), ('OT', 'Other travel'), ('SE', 'Staff entertainment'), ('SU', 'Subsistence')], default='OT', max_length=2),
        ),
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=2282743108864, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.TextField(default='Provide date as DD/MM/YY or date range as DD/MM/YY-DD/MM/YY.', max_length=6),
        ),
        migrations.AlterField(
            model_name='expense',
            name='information',
            field=models.TextField(default='Explaination of expense, including names for entertaining expenses and postcodes for mileage claims.', max_length=500),
        ),
        migrations.AlterField(
            model_name='expense',
            name='persons_seen',
            field=models.TextField(default='Provide the name(s) of the person you saw.', max_length=200),
        ),
    ]
