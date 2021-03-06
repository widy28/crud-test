from django.views.generic import View, TemplateView, DetailView
from models import Leads, LeadsForm
from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         HttpResponse, HttpResponseBadRequest, Http404)
from django.core.urlresolvers import reverse
from django.forms import inlineformset_factory


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
        # languagefromset = inlineformset_factory(Leads, Languages, fields=('languages',))
        # print languagefromset,'======================='
        # print self.form.is_valid(),'-------'
        # f = languagefromset(request.POST, request.FILES, instance= )
        # print f,'---------------'
        if self.form.is_valid():
            print '11111111111'
            data = self.form.cleaned_data
            print data

            # f = languagefromset(request.POST, request.FILES, instance=l)
            self.form.save()
            return HttpResponseRedirect(reverse('leads:leads-list'))
        else:
            print '22222222222'
        return render(request, self.template_name, {'form': self.form})


class DeleteLeads(View):

    def get(self, request, *args, **kwargs):

        lid = kwargs.get('id', '')     # '1'
        lids = kwargs.get('ids', '')   # '1,2,3,4,5'
        if lid:
            l = Leads.objects.filter(id=int(lid))
            if l and len(l) == 1:
                l.delete()
        if lids:
            lids_list = [int(l) for i in lids.split(',')]
            leads = Leads.objects.filter(pk__in=lids_list)
            if leads:
                leads.delete()
        return HttpResponseRedirect(reverse('leads:leads-list'))