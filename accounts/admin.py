from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ("username", "email", "is_admin", "department" )
    list_filter = ("is_admin", "user_type",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "user_type",
                )
            },
        
        ),
        (
            "Permissions", 
            {"fields": (
                "is_active",
                )
            }
        ),
    )

    search_fields = ("username", "email")
    ordering = ("username", "email")

    filter_horizontal = ()


admin.site.register(models.Account, AccountAdmin)


for model in models.register_models:
    class _(admin.ModelAdmin):
        ...

    try:
        _meta = getattr(model, '_Meta')
        
        for attr, value in _meta.admin_attrs.items():
            setattr(_, attr, value)
        admin.site.register(model, _)
        
    except AttributeError:
        continue
