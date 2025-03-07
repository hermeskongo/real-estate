from django.contrib import admin

from properties.models import Categories, Options, Properties, Buildings, Messages, PropertyGallery


# Register your models here.


class PropertyGalleryInline(admin.TabularInline):
    model = PropertyGallery
    extra = 1
    
    
@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Options)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Properties)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        PropertyGalleryInline,
    ]


@admin.register(Buildings)
class BuildingAdmin(admin.ModelAdmin):
    pass

