# Generated by Django 3.1.4 on 2020-12-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dob', models.DateField()),
                ('race', models.TextField()),
                ('intake_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchQuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptchart.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptchart.patient')),
            ],
            options={
                'verbose_name_plural': 'Research Question Responses',
            },
        ),
    ]
