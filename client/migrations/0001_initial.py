# Generated by Django 5.0.1 on 2024-01-30 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter client name', max_length=100, null=True, verbose_name='Client name')),
                ('username', models.CharField(blank=True, help_text='Enter client username', max_length=100, null=True, verbose_name='Client username')),
                ('telegram_id', models.CharField(help_text='Enter telegram ID', max_length=30, unique=True, verbose_name='Telegram ID')),
                ('language', models.CharField(default='uz', help_text='Enter client system language', max_length=10, verbose_name='Client System Language')),
                ('phone', models.CharField(blank=True, help_text='Enter client phone', max_length=100, null=True, verbose_name='Client Phone Number')),
            ],
            options={
                'verbose_name': 'Client ',
                'verbose_name_plural': 'Clients ',
                'db_table': 'Cleints',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(help_text='Enter client latitude', max_length=50, verbose_name='Client latitude')),
                ('longitude', models.CharField(help_text='Enter client longitude', max_length=50, verbose_name='Client longitude')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='client.client', to_field='telegram_id')),
            ],
            options={
                'verbose_name': 'Address ',
                'verbose_name_plural': 'Address ',
                'db_table': 'Address',
            },
        ),
    ]
