# Generated by Django 2.2.3 on 2019-12-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('wicket', models.IntegerField()),
                ('overs', models.IntegerField()),
            ],
        ),
    ]
