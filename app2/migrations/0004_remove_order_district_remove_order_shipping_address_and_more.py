# Generated by Django 5.1.1 on 2024-09-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_alter_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='district',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
