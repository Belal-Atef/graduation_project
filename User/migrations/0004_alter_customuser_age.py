# Generated by Django 3.2 on 2023-05-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_customuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.CharField(max_length=3),
        ),
    ]
