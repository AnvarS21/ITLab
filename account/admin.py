from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SocialLinks


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'position', 'is_staff', 'get_social_links')
    list_filter = ('position', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username', 'position')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('image', 'about_me', 'position')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    def get_social_links(self, obj):
        social_links = obj.social
        return ", ".join(
            [f"{field.verbose_name}: {getattr(social_links, field.name)}" for field in SocialLinks._meta.fields[1:]])

    get_social_links.short_description = 'Соц. сети'


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram', 'facebook', 'instagram', 'linkedin', 'github', 'site_cv', 'vk')
    list_filter = ('user',)
    search_fields = ('user__email', 'user__username')


admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)