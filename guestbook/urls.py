from django.conf.urls.defaults import *

from registration.views import register

from guestbook import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='guestbook_index'),
	(r'^new', views.new_message),
	(r'^accounts/register/$', register, { 'backend': 'guestbook.backends.simple.SimpleBackend' }),
	(r'^accounts/', include('registration.backends.default.urls')),
)