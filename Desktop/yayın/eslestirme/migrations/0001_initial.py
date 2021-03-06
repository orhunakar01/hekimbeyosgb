# Generated by Django 2.2 on 2020-10-19 13:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('isyeriekle', '0001_initial'),
        ('calisilanFirma', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eslestirme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atamaTarihi', models.DateField(default=datetime.date.today, verbose_name='Personeller Atanma Tarihi')),
                ('Sirket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sirket', to='isyeriekle.isyeri')),
                ('firmaAdi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Firma_Adi', to='calisilanFirma.calisilanFirmalar')),
                ('firmaSicil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firma_sicilleri_olacak', to='calisilanFirma.calisilanFirmalar')),
                ('yetkiliHekim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_hekim', to=settings.AUTH_USER_MODEL)),
                ('yetkiliOsgbUzmani_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm', to=settings.AUTH_USER_MODEL)),
                ('yetkiliOsgbUzmani_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_osgb_uzm_2', to=settings.AUTH_USER_MODEL)),
                ('yetkiliSaglikPersoneli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Yetki_sag_pers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
