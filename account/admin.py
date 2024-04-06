from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SocialLinks


class SocialLinksInline(admin.StackedInline):  # или TabularInline, в зависимости от предпочтений по отображению
    model = SocialLinks
    can_delete = False
    verbose_name_plural = 'Социальные ссылки'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'position', 'is_staff')
    list_filter = ('position', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username', 'position')
    ordering = ('email',)
    filter_horizontal = ()
    inlines = [SocialLinksInline]  # Добавляем инлайн для социальных ссылок

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


admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)