# Generated by Django 2.2 on 2024-06-02 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20240602_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
