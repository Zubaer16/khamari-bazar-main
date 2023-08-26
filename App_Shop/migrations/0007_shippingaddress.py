# Generated by Django 4.2.4 on 2023-08-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0006_alter_products_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contat_person_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=300)),
                ('apartment_no', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Shipping Address',
            },
        ),
    ]
