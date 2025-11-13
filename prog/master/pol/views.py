from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, UpdateView, CreateView
from django.urls import reverse_lazy

"""Представление для отображения списка партнеров"""
class PartnerList(TemplateView):
    template_name = 'partner_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context
    
"""Представление для создания нового партнера"""   
class CreatePartner(CreateView):
    template_name = 'create_partner.html'
    model = Partner
    fields = '__all__'
    success_url = reverse_lazy('home')

"""Представление для редактирования партнера"""
class UpdatePartner(UpdateView):
    template_name = 'update_partner.html'
    model = Partner
    fields = '__all__'
    success_url = reverse_lazy('home')

"""Представление для отображения списка продаж"""
class SaleList(TemplateView):
    template_name = 'sale_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sale.objects.all()
        return context

"""Представление для создания новой продажи"""
class CreateSale(CreateView):
    template_name = 'create_sale.html'
    model = Sale
    fields = '__all__'
    success_url = reverse_lazy('sale')