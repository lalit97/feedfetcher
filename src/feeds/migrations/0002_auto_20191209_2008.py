# Generated by Django 2.2.3 on 2019-12-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='overs',
            field=models.FloatField(),
        ),
    ]
