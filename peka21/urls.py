from django import views
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('peserta/',peserta, name='peserta'),
    path('daftar/',daftar, name='daftar'),

    path('peserta/ubah/<int:id_peserta>', EditPeserta, name='edit'),
    path('peserta/detail/<int:pk>',detail, name='detail'),
    path('peserta/delete/<int:pk>', delete, name='delete'),

]
