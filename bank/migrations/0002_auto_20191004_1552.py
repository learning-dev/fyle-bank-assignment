# Generated by Django 2.2.6 on 2019-10-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='addres',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(max_length=50),
        ),
    ]
