# Generated by Django 3.2 on 2023-05-29 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room', models.CharField(max_length=6, unique=True)),
                ('notes_room', models.TextField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_bed', models.CharField(max_length=4)),
                ('Patient_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Patient_id', models.CharField(blank=True, max_length=14, null=True)),
                ('Patient_gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('second_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.TextField(blank=True, max_length=100)),
                ('notes_bed', models.TextField(blank=True, max_length=3000, null=True)),
                ('active', models.BooleanField(default=True)),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
        ),
    ]
