# Generated by Django 2.2 on 2019-09-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20190919_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='num_locations',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
