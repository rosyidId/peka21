# Generated by Django 2.2.10 on 2021-08-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('tempat_lahir', models.CharField(blank=True, max_length=255, null=True)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=255)),
                ('jurusan', models.CharField(max_length=255)),
                ('nomer_telpon', models.BigIntegerField()),
                ('sosmed', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
    ]