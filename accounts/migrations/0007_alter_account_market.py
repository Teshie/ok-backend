# Generated by Django 4.0.4 on 2022-11-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='market',
            field=models.CharField(default='market', max_length=30),
        ),
    ]