# Generated by Django 4.0.4 on 2022-11-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_reports_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdepartment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]