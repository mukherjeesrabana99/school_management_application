# Generated by Django 3.1.2 on 2020-10-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='reg_no',
            field=models.IntegerField(default=728784, unique=True),
        ),
    ]
