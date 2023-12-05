# Generated by Django 4.2.7 on 2023-12-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted'), ('draft', 'Draft'), ('waitingapproval', 'Waiting approval')], default='active', max_length=50),
        ),
    ]
