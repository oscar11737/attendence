# Generated by Django 3.0.6 on 2020-05-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('nAdults', models.IntegerField(default=0)),
                ('nUnder12', models.IntegerField(default=0)),
                ('nAbove12', models.IntegerField(default=0)),
                ('nMeals', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IntermediateRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('nAdults', models.IntegerField(default=0)),
                ('nUnder12', models.IntegerField(default=0)),
                ('nAbove12', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField(unique=True)),
                ('family', models.ManyToManyField(to='attendFellowship.Family')),
            ],
        ),
    ]
