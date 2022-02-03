# Generated by Django 4.0.1 on 2022-02-03 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0031_alter_expense_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=2318025831920, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateTimeField(max_length=25),
        ),
        migrations.AlterField(
            model_name='expense',
            name='persons_seen',
            field=models.CharField(default='Provide the name(s) of the person you saw.', max_length=50),
        ),
    ]