# Generated by Django 4.0.1 on 2022-01-30 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0020_alter_expense_employee_alter_expense_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=1804592030512, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]