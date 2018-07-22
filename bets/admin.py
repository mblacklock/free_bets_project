from django.contrib import admin

from bets.models import Affiliate, Item, Summary

# Register your models here.

class AffiliateAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'freebet']
    list_display = ('name', 'url', 'freebet')

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    
class SummaryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Affiliate, AffiliateAdmin)
admin.site.register(Summary, SummaryAdmin)
