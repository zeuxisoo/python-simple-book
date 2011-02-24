from django import template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def form_all_error(form):
	errors = []
	global_error = form.errors.get('__all__', '')

	if global_error:
		global_error = global_error.as_text()

	for name, field in form.fields.items():
		e = form.errors.get(name, '')
		
		if e:
			errors.append((field.label, force_unicode(e), ))

	return mark_safe(u'<ul class="error-list">%s %s</ul>' % (global_error, ''.join([u'%s %s' % (k, v) for k, v in errors])))