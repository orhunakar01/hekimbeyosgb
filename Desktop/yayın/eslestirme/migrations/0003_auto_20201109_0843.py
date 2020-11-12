# Generated by Django 2.2 on 2020-11-09 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eslestirme', '0002_auto_20201105_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliHekim',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_hekim', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliOsgbUzmani_2',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliOsgbUzmani_3',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm_3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliOsgbUzmani_4',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm_4', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliOsgbUzmani_5',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm_5', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eslestirme',
            name='yetkiliSaglikPersoneli',
            field=models.ForeignKey(blank=True, default='YOK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_sag_pers', to=settings.AUTH_USER_MODEL),
        ),
    ]
