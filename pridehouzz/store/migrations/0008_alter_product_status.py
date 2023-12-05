# Generated by Django 4.2.7 on 2023-12-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted'), ('waitingapproval', 'Waiting approval'), ('draft', 'Draft')], default='active', max_length=50),
        ),
    ]