from django.conf.urls import patterns, url

from .views import LeadsList, AddLeadView, DeleteLeads

urlpatterns = patterns(
    '',
    url(r'^$', LeadsList.as_view(), name='leads-list'),
    url(r'^addlead/$', AddLeadView.as_view(), name='leads-add'),
    url(r'^delete/(?P<id>\d+)', DeleteLeads.as_view(), name='delete-lead'),
    url(r'^delete/(?P<ids>\d+)', DeleteLeads.as_view(), name='delete-leads'),
)
