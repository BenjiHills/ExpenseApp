# Generated by Django 4.0.1 on 2022-01-23 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0007_rename_manager_comment_expenses_manager_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Expense',
        ),
    ]
