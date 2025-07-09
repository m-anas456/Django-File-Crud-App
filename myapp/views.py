from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import UploadedFile

class FileListView(ListView):
    model = UploadedFile
    template_name = 'fileapp/file_list.html'
    context_object_name = 'files'

class FileDetailView(DetailView):
    model = UploadedFile
    template_name = 'fileapp/file_detail.html'

class FileCreateView(CreateView):
    model = UploadedFile
    fields = ['file', 'description']
    template_name = 'fileapp/file_form.html'
    success_url = reverse_lazy('file-list')

class FileUpdateView(UpdateView):
    model = UploadedFile
    fields = ['file', 'description']
    template_name = 'fileapp/file_form.html'
    success_url = reverse_lazy('file-list')

class FileDeleteView(DeleteView):
    model = UploadedFile
    template_name = 'fileapp/file_confirm_delete.html'
    success_url = reverse_lazy('file-list')
