from django.db.models import Model
from django.shortcuts import render
from django.views.generic import TemplateView

from ongs.models import Ongs


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ongs'] = Ongs.objects.filter(is_active=True)
        return context