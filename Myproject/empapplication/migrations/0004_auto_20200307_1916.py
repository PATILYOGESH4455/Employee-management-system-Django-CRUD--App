# Generated by Django 3.0.2 on 2020-03-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapplication', '0003_auto_20200307_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee_id',
            field=models.IntegerField(),
        ),
    ]
