from django.contrib import admin
from App.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'occupation', 'salary', 'gender', 'created_at']
	search_fields = ['name', 'email', 'occupation', 'salary']
	list_filter = ['gender']
	list_per_page = 8

admin.site.register(Contact, ContactAdmin)