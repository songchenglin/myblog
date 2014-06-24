from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

import this
# Create your views here.
class HomeView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'zens'
    def get_queryset(self):
        return this.L
