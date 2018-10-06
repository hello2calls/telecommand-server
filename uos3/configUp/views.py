﻿from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import config
from .forms import configCreateForm, configModForm
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'configUp/index.html'


class ThanksView(generic.TemplateView):
    template_name = 'configUp/configThanks.html'


class ConfigUpView(generic.TemplateView):
    template_name = 'configUp/configUp.html'

    def get(self, request, *args, **kwargs):
        if self.template_name == 'configUp/configUp.html':
            form = configCreateForm(initial={
                'power_rail_1': 1,
                'power_rail_3': 1,
                'power_rail_5': 1,
                'power_rail_6': 1,
            })
        else:
            form = configModForm(initial={
            })
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if self.template_name == 'configUp/configUp.html':
            form = configCreateForm(request.POST)
        else:
            form = configModForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('configThanks')


class ListConfigsView(generic.ListView):
    model = config
    template_name = 'configUp/listConfigs.html'


# class DetView(generic.DetailView):
#     model = config
#     template_name = 'configUp/detail.html'
