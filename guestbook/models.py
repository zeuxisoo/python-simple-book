from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

class Message(models.Model):
	leave_by = models.ForeignKey(User)
	subject = models.CharField(max_length=200)
	content = models.TextField(default='')
	create_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.subject
		
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='pybook_profile', verbose_name=_("User"))
	last_leave_message_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.user.username

#
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
	
def update_user_profile_by_message(sender, instance, created, **kwargs):
	if created:
		p = instance.leave_by.pybook_profile
		p.last_leave_message_date = instance.create_date
		p.save()
		
post_save.connect(create_user_profile, sender=User)
post_save.connect(update_user_profile_by_message, sender=Message)

		
