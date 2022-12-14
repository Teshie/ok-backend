# Generated by Django 4.0.4 on 2022-12-03 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billings', '0003_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='store',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL),
        ),
    ]
