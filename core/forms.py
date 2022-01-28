from django import forms
from core import models
from django.forms import widgets
from django.utils.regex_helper import Choice

class FormPeserta(forms.Form):
    nama = forms.CharField(label="Nama",
        widget=forms.TextInput(
            attrs={
                "label" : "Nama",
                "placeholder" : "Nama Lengkap",
                "class" : "form-control"

            }
    )   )
    alamat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Alamat",
                "class" : "form-control"
            }
        )
    )
    tempat_lahir = forms.CharField(label="Tempat Lahir",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tempat Lahir",
                "class" : "form-control"
            }
    )   )
    tanggal_lahir = forms.DateField(label="Tanggal Lahir",
        widget=forms.DateInput(
            attrs={
                "class" : "form-control",
                "type" : "date"
            }
        )
    )
    GENDER = [
        ("Laki - Laki", "Laki - Laki"),
        ("Perempuan", "Perempuan")
    ]

    jenis_kelamin = forms.ChoiceField(label="Jenis Kelamin", 
        widget=forms.Select(
            attrs={
                "placeholder" : "Jenis Kelamin",
                "class" : "form-control"
            },
        ),
        choices=GENDER
    )
    PRODI = [
        ("TI","Teknik Informatika"),
        ("SI","Sistem Informasi")
    ]
    jurusan = forms.ChoiceField(label="Program Studi",
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        choices=PRODI
    )
    
    nomer_telpon = forms.IntegerField(label="Nomor HP/WA",
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "ex. 08xxxxxxxxxx",
                "class" : "form-control"
            }
        )
    )

    email = forms.EmailField(label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "xxxxxxx@gmail.com",
                "class" : "form-control"
            }
        )
    )