# Generated by Django 3.1.2 on 2020-10-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.IntegerField(default=462815, unique=True),
        ),
    ]
