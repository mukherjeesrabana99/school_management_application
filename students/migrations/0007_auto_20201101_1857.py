# Generated by Django 3.1.2 on 2020-11-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20201101_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.IntegerField(default=411041, unique=True),
        ),
    ]
