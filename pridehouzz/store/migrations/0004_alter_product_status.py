# Generated by Django 4.2.7 on 2023-12-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('waitingapproval', 'Waiting approval'), ('deleted', 'Deleted'), ('active', 'Active'), ('draft', 'Draft')], default='active', max_length=50),
        ),
    ]