# Generated by Django 2.2.5 on 2019-09-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]