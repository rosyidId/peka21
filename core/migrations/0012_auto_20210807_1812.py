# Generated by Django 2.2.10 on 2021-08-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210807_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]