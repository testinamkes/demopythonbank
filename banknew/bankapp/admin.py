from django.contrib import admin
from .models import District, Branch

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'wikipedia_link')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'loan_price', 'available_loan', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('district', 'available_loan')
    search_fields = ('name', 'district__name')
