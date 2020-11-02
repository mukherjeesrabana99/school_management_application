# Generated by Django 3.1.2 on 2020-10-31 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('day1', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=30)),
                ('day2', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=30)),
                ('day3', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=30)),
                ('day4', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=30)),
                ('day5', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=30)),
                ('sub1_time', models.TimeField()),
                ('sub2_time', models.TimeField()),
                ('break_time', models.TimeField()),
                ('scl_over_time', models.TimeField()),
                ('class_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.registeredclass')),
                ('sub1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub1', to='academics.subject')),
                ('sub2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub2', to='academics.subject')),
            ],
        ),
    ]
