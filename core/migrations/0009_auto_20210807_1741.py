# Generated by Django 2.2.10 on 2021-08-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210807_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peserta',
            old_name='sosmed',
            new_name='email',
        ),
    ]
