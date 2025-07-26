from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (fieldsets[1][0], {'fields': fieldsets[1][1]['fields'] + ('user_type',) + ('skin_type',) 
                                      + ('concern',) + ('preferences',) + ('device_type',) + ('created_at',) })

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type', 'skin_type', 'concern', 'preferences','device_type' ,'created_at' ),  
        }),
    )

    list_display = UserAdmin.list_display + ('email', 'user_type', 'skin_type','concern', 'preferences','device_type' ,'created_at' )
    list_filter = UserAdmin.list_filter + ('user_type',) + ('skin_type',) + ('concern',) + ('preferences',) + ('device_type',) + ('created_at',) 
