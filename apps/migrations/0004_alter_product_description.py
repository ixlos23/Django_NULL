# Generated by Django 5.1.2 on 2024-11-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='ab', max_length=255, null=True),
        ),
    ]
