# Generated by Django 2.2 on 2020-11-09 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dosyayukle', '0014_remove_dosyayukle_osgbuzmanadi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosyayukle',
            name='Olusturan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Olusturan', to=settings.AUTH_USER_MODEL, verbose_name='Görevli Personel'),
        ),
    ]
