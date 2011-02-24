from django import forms
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail

from models import Message, UserProfile

class MessageForm(forms.ModelForm):
	subject = forms.CharField(label=_('Subject'), widget=forms.TextInput(attrs={'size':'30'}))
	content = forms.CharField(label=_('Content'), widget=forms.Textarea(attrs={'cols':'95', 'rows':'14'}))
	
	class Meta:
		model = Message
		fields = ['subject', 'content']
		
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user", None)
		
		super(MessageForm, self).__init__(*args, **kwargs)
	
	def save(self):
		message = Message(
			leave_by=self.user,
			subject=self.cleaned_data['subject'],
			content=self.cleaned_data['content']
		)
		message.save()
		return message

class RegisterForm(RegistrationFormUniqueEmail):
	username = forms.RegexField(
		regex=r'(?u)^\w+$', 
		max_length=30,
		widget=forms.TextInput(),
		label=_("Username"),
		error_messages={
			'invalid': _("This value must letters only, numbers and underline only.")
		}
	)