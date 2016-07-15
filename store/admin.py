from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'make','stock', 'price')

admin.site.register(Item, ItemAdmin)
