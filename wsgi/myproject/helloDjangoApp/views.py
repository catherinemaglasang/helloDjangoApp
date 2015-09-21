from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from helloDjangoApp.models import HelloDjangoApp

# Create your views here.


def hello(request):
    return HttpResponse("Hello World!")


class HelloDjangoAppList(ListView):
    model = HelloDjangoApp


class HelloDjangoAppCreate(CreateView):
    model = HelloDjangoApp
    success_url = reverse_lazy('helloDjangoApp_list')
    fields = ['name', 'ip', 'order']


class HelloDjangoAppUpdate(UpdateView):
    model = HelloDjangoApp
    success_url = reverse_lazy('helloDjangoApp_list')
    fields = ['name', 'ip', 'order']


class HelloDjangoAppDelete(DeleteView):
    model = HelloDjangoApp
    success_url = reverse_lazy('helloDjangoApp_list')
