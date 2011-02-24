from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from pybook import settings
from models import Message
from forms import MessageForm, RegisterForm

def index(request):
	message_form = MessageForm()
	messages = Message.objects.all().order_by('-create_date')
	
	return render_to_response("guestbook/index.html", {
		"settings": settings,
		"message_form": message_form,
		"messages": messages
	}, RequestContext(request))
	
@login_required
def new_message(request):
	pass
	if request.method == "POST":
		message_form = MessageForm(request.POST, user=request.user)
		messages = Message.objects.all().order_by('-create_date')

		if message_form.is_valid() and request.POST.get('commit', ''):
			post = message_form.save()
			return HttpResponseRedirect(reverse("guestbook_index")) 
		
		return render_to_response("guestbook/index.html", {
			"settings": settings,
			"message_form": message_form,
			"messages": messages,
		}, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse("guestbook_index"))