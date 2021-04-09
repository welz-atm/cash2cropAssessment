from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'state_of_residence', )


admin.site.register(CustomUser, UserAdmin)



