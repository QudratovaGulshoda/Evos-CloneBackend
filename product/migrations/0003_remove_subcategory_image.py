# Generated by Django 5.0.1 on 2024-01-31 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_subcategory_options_alter_subcategory_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
    ]