# Generated by Django 5.1.6 on 2025-04-18 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=40)),
                ('mother_name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('pincode', models.PositiveIntegerField()),
                ('phone', models.PositiveBigIntegerField(unique=True)),
                ('mail', models.EmailField(max_length=254)),
                ('adhar_num', models.BigAutoField(default=123456789010, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='profiles')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.gender')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.state')),
            ],
        ),
    ]
