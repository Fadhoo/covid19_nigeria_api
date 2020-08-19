# Generated by Django 3.0.5 on 2020-08-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncdc_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coviddata',
            name='active_cases',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='confirmed_cases',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='deaths',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='discharged_cases',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coviddata',
            name='samples_tested',
            field=models.CharField(max_length=10),
        ),
    ]
