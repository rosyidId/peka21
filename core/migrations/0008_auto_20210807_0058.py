# Generated by Django 2.2.10 on 2021-08-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210807_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='nomer_telpon',
            field=models.BigIntegerField(null=True),
        ),
    ]