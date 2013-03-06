from django.conf.urls import patterns, include, url
from dj_ampta_1dv450_cr222cs import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^dj_ampta_1dv450_cr222cs/', include('dj_ampta_1dv450_cr222cs.foo.urls')),

    url(r'^$', 'ampta.helper.views.login_user', name='home'),

    url(r'^login/$', 'ampta.helper.views.login_user', name="login"),
    url(r'^logout/$', 'ampta.helper.views.logout_user', name="logout"),

    url(r'^search/$', 'ampta.project_view.views.search', name="search"),

    url(r'^projects/$', 'ampta.project_view.views.index', name="project_list"),
    url(r'^project/add$', 'ampta.project_view.views.add', name="project_add"),
    url(r'^project/(?P<project_id>\d+)/delete/$', 'ampta.project_view.views.delete', name="project_delete"),
    url(r'^project/(?P<project_id>\d+)/edit/$', 'ampta.project_view.views.edit', name="project_edit"),
    url(r'^project/(?P<project_id>\d+)/$', 'ampta.project_view.views.detail', name="project_link"),

    url(r'^project/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)/$', 'ampta.ticket_view.views.detail', name="project_ticket"),
    url(r'^project/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)/delete/$', 'ampta.ticket_view.views.delete', name="ticket_delete"),
    url(r'^project/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)/edit/$', 'ampta.ticket_view.views.edit', name="ticket_edit"),
    url(r'^project/(?P<project_id>\d+)/ticket/add/$', 'ampta.ticket_view.views.add', name="ticket_add"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)