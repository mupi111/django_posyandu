from django.shortcuts import render
from .models import Siposyandu 
from django.views.generic import DetailView, CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.
data = Siposyandu.objects.all()
var = {
    'judul':'Sistem Informasi Posyandu',
    'info' :'Sistem ini mengelola data anak dan ibu di Posyandu Desa Gempolan',
    'oleh':'admin-Nurul Mufidatul Maisaroh',
    'siposyandu':data}

def index(self):
    var['siposyandu'] = Siposyandu.objects.values('id','nik','nama','jk','tmpt_lahir').\
        order_by('id')
    return render(self,'siposyandu/index.html',context=var)

class PosDetailView(DetailView):
    model = Siposyandu
    template_name = 'siposyandu/pos_detail_view.html'

    def get_context_data(self, **kwargs):
        context = var
        context.update(super().get_context_data(**kwargs))
        return context

class PosCreateView(SuccessMessageMixin,CreateView):
    model = Siposyandu
    fields = '__all__'
    template_name = 'siposyandu/pos_add.html'
    success_url = reverse_lazy('home_page')
    success_massage = 'Berhasil menambahkan data'

    def get_context_data(self, **kwargs):
        context = var
        context.update(super().get_context_data(**kwargs))
        return context

class PosUpdateView(SuccessMessageMixin,UpdateView):
    model = Siposyandu
    fields = '__all__'
    template_name = 'siposyandu/pos_edit.html'
    success_url = reverse_lazy('home_page')
    success_massage = 'Berhasil mengedit data'

    def get_context_data(self, **kwargs):
        context = var
        context.update(super().get_context_data(**kwargs))
        return context

class PosDeleteView(DeleteView):
    model = Siposyandu
    template_name = 'siposyandu/pos_delete.html'
    success_url = reverse_lazy('home_page')

    # def get_context_data(self, **kwargs):
    #     context = var
    #     context.update(super().get_context_data(**kwargs))
    #     return context

def PosToPdf(request):
    dataprint = {
    'siposyandu' : Siposyandu.objects.values('nik','nama','tmpt_lahir','jk','bb','tb','nama_ayah','nama_ibu','agama'),
    'request': request,
    }
    html = loader.render_to_string('siposyandu/pos_pdf.html', dataprint)
    output = pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response