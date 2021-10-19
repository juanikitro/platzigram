"""User admin classes"""
# Django
from django.contrib import admin

# Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin class"""

    # Cambiamos vista de tabla
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture') 
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
            'user__email',
            'user__username',
            'user__first_name', 
            'user__last_name', 
            'user__phonenumber'
        )
    fieldsets = (
        ('Profile',{
            'fields': (
                'user',
                'picture',
            ),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography',),
            ),
        }),
    )