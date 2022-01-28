from django.db import models

# Create your models here.

class Jurusan(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class JenisKelamin(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Peserta(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=255, blank=True, null=True)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=255, null=True)
    jurusan = models.CharField(max_length=255, null=True)
    nomer_telpon = models.BigIntegerField(null=True)
    email = models.CharField(max_length=255, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nama
        
    

