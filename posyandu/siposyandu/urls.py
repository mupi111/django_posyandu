from django.urls import path
from .views import index, PosDetailView,PosCreateView
from .views import PosUpdateView,PosDeleteView,PosToPdf

urlpatterns = [ 
     path('', index, name='home_page'),
     path('siposyandu/<int:pk>', PosDetailView.as_view(), name='pos_detail_view'),
     path('siposyandu/add', PosCreateView.as_view(), name='pos_add'),
     path('siposyandu/edit/<int:pk>', PosUpdateView.as_view(), name='pos_edit'),
     path('siposyandu/delete/<int:pk>', PosDeleteView.as_view(), name='pos_delete'),
     path('siposyandu/print_pdf', PosToPdf, name='pos_pdf'),
]
