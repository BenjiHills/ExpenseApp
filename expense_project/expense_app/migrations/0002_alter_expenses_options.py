# Generated by Django 4.0.1 on 2022-01-23 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['Time']},
        ),
    ]
