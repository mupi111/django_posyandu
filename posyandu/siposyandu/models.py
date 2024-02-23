from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# Create your models here.

class Siposyandu(models.Model):
     JK_CHOICES = (('l','Laki-laki'),('p','Perempuan'))
     AG_CHOICES = (('is','Islam'),('kk','Kristen Katolik'),
                   ('kp','Kristen Protestan'),('hi','Hindu'),('bu','Budha'))
  
     nik = models.CharField('NIK', max_length=17)  
     nama = models.CharField('Nama Anak', max_length=50, null=False)
     tmpt_lahir = models.CharField('Tempat Lahir', max_length=30)
     jk = models.CharField('Jenis Kelamin', max_length=2, choices=JK_CHOICES)
     bb = models.IntegerField()
     tb = models.IntegerField()
     nama_ayah = models.CharField('Nama Ayah', max_length=50)
     nama_ibu = models.CharField('Nama Ibu', max_length=50)
     agama = models.CharField('Agama', max_length=50, choices=AG_CHOICES)

# class Meta:
#     ordering = ['-tgl_input']

def __str__(self):
    return self.nama

def get_absolute_url(self):
    return reverse('home_page')
    