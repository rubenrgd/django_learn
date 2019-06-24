from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'hostname', 'is_published', 'bought_price', 'list_date', 'realtor')
    list_display_links = ('id', 'hostname')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('hostname', 'env')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)
