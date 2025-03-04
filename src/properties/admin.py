from django.contrib import admin

from properties.models import Categories, Options, Properties, Buildings

# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Options)
class OptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Properties)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Buildings)
class BuildinAdmin(admin.ModelAdmin):
    pass
