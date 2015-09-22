from django.views.generic import TemplateView, DetailView
from models import Leads, LeadsForm
from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         HttpResponse, HttpResponseBadRequest, Http404)
from django.core.urlresolvers import reverse


class LeadsList(TemplateView):
    template_name = 'leads/list.html'

    def get_context_data(self, **kwargs):
        ctx = super(LeadsList, self).get_context_data(**kwargs)
        leads = Leads.objects.all()
        ctx['leads'] = leads
        return ctx

class AddLeadView(TemplateView):
    template_name = 'leads/addlead.html'
    form_class = LeadsForm
    model = Leads

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(self.request.POST)
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):

        self.form = self.form_class(self.request.POST)
        print self.form.is_valid(),'-------'
        if self.form.is_valid():
            print '11111111111'
            data = self.form.cleaned_data
            print data
            self.form.save()
            return HttpResponseRedirect(reverse('leads:leads-list'))
        else:
            print '22222222222'
        return render(request, self.template_name, {'form': self.form})

