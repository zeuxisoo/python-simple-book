from django.contrib import admin

from guestbook.models import Message, UserProfile

class MessageAdmin(admin.ModelAdmin):
	list_display = ('leave_by', 'subject', 'content', 'create_date')
	list_filter = ('leave_by',)
	search_field = ('leave_by__username', 'subject', 'message')
	
admin.site.register(Message, MessageAdmin)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'last_leave_message_date')
	search_fields = ('user__username',)

admin.site.register(UserProfile, UserProfileAdmin)