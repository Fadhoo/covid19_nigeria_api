# Generated by Django 3.0.5 on 2020-08-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('samples_tested', models.IntegerField()),
                ('confirmed_cases', models.IntegerField()),
                ('active_cases', models.IntegerField()),
                ('discharged_cases', models.IntegerField()),
                ('deaths', models.IntegerField()),
            ],
        ),
    ]