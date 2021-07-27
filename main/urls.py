from django.urls import path

from main.views import CountryView

urlpatterns = [
    path('', CountryView.as_view(), name='index')
]