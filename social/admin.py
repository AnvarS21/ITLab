from django.contrib import admin
from .models import Gallery, News, NewsImage, AboutUs, AboutUsImages


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)


class NewsImageInline(admin.TabularInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'created_at', 'updated_at')
    search_fields = ('title', 'speaker')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'speaker', 'preview')
        }),
        ('Дата и время', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [NewsImageInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('preview',)
        return self.readonly_fields


class AboutUsImagesInline(admin.TabularInline):
    model = AboutUsImages


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('body',)
    search_fields = ('body',)
    inlines = [AboutUsImagesInline]





