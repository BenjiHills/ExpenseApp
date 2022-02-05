# Generated by Django 4.0.1 on 2022-02-04 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0037_remove_expense_expense_date_alter_expense_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='date_expense',
            new_name='expense_date',
        ),
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=1592022602864, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
