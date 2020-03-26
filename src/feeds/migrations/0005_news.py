# Generated by Django 2.2.3 on 2019-12-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20191209_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]