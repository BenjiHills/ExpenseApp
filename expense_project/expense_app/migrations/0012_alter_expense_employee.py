# Generated by Django 4.0.1 on 2022-01-24 03:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0011_rename_expense_amount_expense_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(on_delete=models.SET('User Deleted'), to=settings.AUTH_USER_MODEL),
        ),
    ]
