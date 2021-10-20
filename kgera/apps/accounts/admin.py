from django.contrib import admin
from  .models import User, Profile

# Register your models here.

class ProfileInline(admin.TabularInline):
    model = Profile


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['username']}), ('First Name', {'fields': ['first_name']}), ('Last Name', {'fields': ['last_name']}), ('User Level', {'fields': ['user_type'], 'classes': ['collapse']}),]
    inlines = [ProfileInline]

admin.site.register(User, ProfileAdmin)