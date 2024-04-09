from django.contrib import admin
from .models import Review, Student, Client


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user',)
    list_filter = ('created_at',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email')
    list_filter = ('phone_number',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'company')
    search_fields = ('full_name', 'email', 'company')
    list_filter = ('company',)
