from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_at']
    readonly_fields = ['name', 'email', 'subject', 'message']


admin.site.register(Contact, ContactAdmin)