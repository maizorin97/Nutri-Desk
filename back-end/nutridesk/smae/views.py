from django.shortcuts import render

from django.views.generic import TemplateView

class info(TemplateView):
    template_name = "info.html"