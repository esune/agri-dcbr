# Generated by Django 2.2 on 2019-08-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20190722_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_factor_operation',
            name='perm_id_other',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='risk_factor_operation',
            name='perm_id_type',
            field=models.CharField(choices=[('TATTOO', 'TATTOO'), ('MICROCHIP', 'MICROCHIP'), ('OTHER', 'OTHER'), ('NOT_APPLICABLE', 'NOT_APPLICABLE')], default='NOT_APPLICABLE', max_length=15),
        ),
    ]
