from django.shortcuts import render


import logging

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic import TemplateView

from . import plots

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "index.html"


class Plot1DView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context["plot"] = plots.plot1d()
        return context


class KenyanMap(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KenyanMap, self).get_context_data(**kwargs)
        context["plot"] = plots.second_kenyan_map()
        return context
