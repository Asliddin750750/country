from django.shortcuts import render

from .models import Country
from django.views.generic import View


class CountryView(View):
    def get(self, request):
        return render(request, 'main/index.html', {
            'countries': Country.objects.all()
        })