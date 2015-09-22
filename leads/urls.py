from django.conf.urls import patterns, url

from .views import LeadsList, AddLeadView

urlpatterns = patterns(
    '',
    url(r'^$', LeadsList.as_view(), name='leads-list'),
    url(r'^addlead/$', AddLeadView.as_view(), name='leads-add'),
)
