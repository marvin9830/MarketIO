# Generated by Django 4.2.4 on 2024-03-16 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_sale_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariant",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variants",
                to="products.product",
            ),
        ),
    ]