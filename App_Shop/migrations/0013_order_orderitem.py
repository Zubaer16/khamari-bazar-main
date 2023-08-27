# Generated by Django 4.2.4 on 2023-08-27 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Shop', '0012_shippingaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('processing', 'processing'), ('accepted', 'accepted'), ('deliverd', 'delivered'), ('cancelled', 'cancelled')], default='processing', max_length=100)),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='App_Shop.shippingaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Shop.products')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Shop.order')),
            ],
        ),
    ]
