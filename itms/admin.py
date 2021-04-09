from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item, Contact


class ItemAdmin(admin.ModelAdmin):
    list_display = ('price', 'description', 'seller', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'item', 'interest', )


admin.site.register(Item, ItemAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)



