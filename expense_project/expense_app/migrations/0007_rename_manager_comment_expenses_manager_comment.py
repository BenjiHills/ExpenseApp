# Generated by Django 4.0.1 on 2022-01-23 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0006_alter_expenses_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='manager_Comment',
            new_name='manager_comment',
        ),
    ]
