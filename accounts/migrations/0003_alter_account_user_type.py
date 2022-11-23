# Generated by Django 4.0.4 on 2022-11-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_subdepartment_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(blank=True, choices=[('CEO', 'Chief Executive Officer'), ('CMO', 'Chief Executive Officer'), ('CFO', 'Chief Executive Officer')], default='CEO', max_length=50, null=True),
        ),
    ]
