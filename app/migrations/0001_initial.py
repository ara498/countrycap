# Generated by Django 5.0.8 on 2024-09-23 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=10)),
                ('dept_loc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SalGrade',
            fields=[
                ('GRADE', models.IntegerField(primary_key=True, serialize=False)),
                ('LowSAL', models.DecimalField(decimal_places=3, max_digits=20)),
                ('HISAL', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('emp_no', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=40)),
                ('cmm', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Hire_date', models.DateField(auto_now_add=True)),
                ('MGR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.employee')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
