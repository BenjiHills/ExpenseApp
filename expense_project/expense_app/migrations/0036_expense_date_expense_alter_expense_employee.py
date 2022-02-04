# Generated by Django 4.0.1 on 2022-02-04 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0035_alter_expense_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date_expense',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=2702355163776, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]