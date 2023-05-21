from django.contrib import admin

from tradingplatform.links.models import Link, Contact, Product


@admin.action(description="Nullifies the debt")
def make_debt_to_zero(Link, request, queryset):
    queryset.update(debt="0")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'debt', 'provider', )
    list_display_links = ('name', 'provider',)
    readonly_fields = ('level',)
    search_fields = ('contacts__City',)
    list_filter = ('contacts__City',)
    actions = [make_debt_to_zero]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Email', 'Country', 'City', 'Street', 'HouseNumber')
    search_fields = ('City',)
    list_filter = ('City',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'DateOfAppearance')
    search_fields = ('name',)
    list_filter = ('name',)
