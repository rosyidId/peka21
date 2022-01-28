from django.contrib.messages.api import MessageFailure
from core.models import Peserta
from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django import template
from core.forms import FormPeserta


# Create your views here.
def dashboard(request):
    return render(request, 'layouts/dashboard.html')

def daftar(request):
    form = forms.FormPeserta(request.POST or None)
    if form.is_valid():
        peserta = Peserta()
        peserta.nama = form.cleaned_data.get('nama')
        peserta.alamat = form.cleaned_data.get('alamat')
        peserta.tempat_lahir = form.cleaned_data.get('tempat_lahir')
        peserta.tanggal_lahir = form.cleaned_data.get('tanggal_lahir')
        peserta.jenis_kelamin = form.cleaned_data.get('jenis_kelamin')
        peserta.jurusan = form.cleaned_data.get('jurusan')
        peserta.nomer_telpon = form.cleaned_data.get('nomer_telpon')
        peserta.email = form.cleaned_data.get('email')

        peserta.save()
        return redirect('peserta')
    template_name = 'peserta/tambah-peserta.html'

    konteks = {
        'title': 'Form Pendaftaran',
        'form' : form,
    }
    return render(request, template_name,konteks)

def EditPeserta(request, id_peserta):
    peserta = get_object_or_404(Peserta, id=id_peserta)
    form =FormPeserta(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('peserta')
    
    template_name = 'peserta/tambah-peserta.html'
    konteks = {
        'title': 'Form Pendaftaran',
        'form' : form,
    }
    return render(request, template_name, konteks)


def peserta(request):
    data = Peserta.objects.all()
    konteks = {
        'title' : 'Daftar Peserta Peka21',
        'object_list': data
    }
    template_name = 'peserta/peserta-list.html'
    return render(request, template_name, konteks)

def detail(request, pk):
    data = get_object_or_404(Peserta, pk=pk)
    konteks = {
        'object' : data
    }

    template_name = 'peserta/peserta_detail.html'
    return render(request, template_name, konteks)

def delete(request, pk):
    peserta = Peserta.objects.filter(id=pk)
    peserta.delete()
    
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('peserta')

# def edit(request, id_peserta):
#     peserta = Peserta.objects.get(id=id_peserta)
#     template = 'peserta/ubah-peserta.html'

#     if request.POST:
#         form =FormPeserta(request.POST, instance=peserta)
#         if form.is_valid():
#             form.save()

#             messages.success(request, "Data Berhasil di Ubah")
#             return redirect('ubah_peserta', id_peserta=id_peserta)
        
#         else:
#             form = FormPeserta(instance=peserta)
#             konteks = {
#                 'form': form,
#                 'peserta':peserta,
#             }
#         return render(request, template, konteks)
    