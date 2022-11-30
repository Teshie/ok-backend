# Generated by Django 4.0.4 on 2022-11-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_profit', models.IntegerField(default=1)),
                ('name', models.CharField(default='name', max_length=100)),
                ('imgUrl', models.TextField(default='')),
                ('selling_price', models.FloatField(default=1)),
                ('actual_price', models.FloatField(default=1)),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('imgUrl', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('imgUrl', models.TextField(default='')),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('actual_price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgUrl', models.TextField(blank=True, null=True)),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('actual_price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]