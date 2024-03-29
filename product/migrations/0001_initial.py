# Generated by Django 5.0.1 on 2024-01-30 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Category name')),
                ('image', models.ImageField(blank=True, help_text="Upload Categories' Image", null=True, upload_to='category-image', verbose_name='Category Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category ',
                'verbose_name_plural': 'Categories ',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='SubCategory name')),
                ('image', models.ImageField(blank=True, help_text="Upload SubCategories' Image", null=True, upload_to='subcategory-image', verbose_name='SubCategory Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Enter product name', max_length=255, verbose_name='Product Name')),
                ('description', models.TextField(help_text="Field for Product's description", verbose_name='About Product')),
                ('price', models.IntegerField(default=0, help_text="Enter product's price", verbose_name="Product's Price")),
                ('discount', models.IntegerField(default=0, help_text="Enter product's discount price", verbose_name="Product's discount price")),
                ('image', models.ImageField(blank=True, help_text="Upload Product's Image", null=True, upload_to='product-image', verbose_name='Product Image')),
                ('category', models.ForeignKey(help_text='Choose Category', on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='product.category', verbose_name="Product's Category")),
                ('subcategory', models.ForeignKey(help_text='Choose Subcategory', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.subcategory', verbose_name="Product's Subcategory")),
            ],
            options={
                'verbose_name': 'Product ',
                'verbose_name_plural': 'Products ',
                'db_table': 'Products',
            },
        ),
    ]
