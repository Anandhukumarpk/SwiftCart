# Generated by Django 5.1.1 on 2024-09-25 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
