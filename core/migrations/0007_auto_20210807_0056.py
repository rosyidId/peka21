# Generated by Django 2.2.10 on 2021-08-07 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210806_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='jenis_kelamin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='jurusan',
            field=models.CharField(max_length=255, null=True),
        ),
    ]