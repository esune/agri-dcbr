# Generated by Django 2.2 on 2019-06-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190618_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='operation_type',
            field=models.CharField(choices=[('BREEDER', 'BREEDER'), ('SELLER', 'SELLER'), ('BREEDER & SELLER', 'BREEDER & SELLER')], default='BREEDER', max_length=20),
        ),
    ]