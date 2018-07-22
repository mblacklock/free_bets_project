from django.contrib import admin

from bets.models import Affiliate, Item, Summary

# Register your models here.

class AffiliateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Affiliate)
admin.site.register(Item)
admin.site.register(Summary)
