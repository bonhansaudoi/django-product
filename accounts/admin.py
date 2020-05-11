from django.contrib import admin
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
 
# from .forms import UserCreationForm, UserChangeForm
from .models import UserAccount 

class UserAdmin(BaseUserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': (
            'first_name', 'avatar'
            )}
        ),
        ( 'Permissions', {
            'fields': (
                'is_active', 
            ),} 
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'is_active')
 
    search_fields = ('email', 'first_name',)
    ordering = ('email',)

    # filter_horizontal = ()
 
admin.site.register(UserAccount, UserAdmin)
admin.site.unregister(Group) 