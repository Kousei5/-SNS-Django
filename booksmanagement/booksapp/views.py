from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BooksList
from django.urls import reverse_lazy

# Create your views here.

class BookList(ListView):
    template_name = 'list.html'
    model = BooksList

class BookDetail(DetailView):
    template_name = 'detail.html'
    model = BooksList

class BookCreate(CreateView):
    template_name='add.html'
    model = BooksList
    fields = ('title', 'memo', 'read', 'p_date')
    success_url = reverse_lazy('list')

class BookDelete(DeleteView):
    template_name = 'delete.html'
    model = BooksList
    success_url = reverse_lazy('list')

class BookUpdate(UpdateView):
    template_name = 'update.html'
    model = BooksList
    fields = ('title', 'memo', 'read', 'p_date')
    success_url = reverse_lazy('list')