# Generated by Django 2.2 on 2020-11-02 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokumanlar', '0016_saha'),
    ]

    operations = [
        migrations.CreateModel(
            name='kurul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sira_no', models.PositiveIntegerField(default=0)),
                ('ismi', models.CharField(max_length=60)),
                ('dosya', models.FileField(upload_to='documents/sablonlar/%Y/%m/%d')),
                ('guncel_tarih', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
