# Generated by Django 5.1.6 on 2025-04-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_fname_aadhar_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar',
            name='adhar_num',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
