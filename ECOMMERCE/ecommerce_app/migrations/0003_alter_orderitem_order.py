# Generated by Django 4.2.7 on 2023-11-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, default=0, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce_app.order'),
        ),
    ]
