from django.contrib import admin

from .models import GetInTouch


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at',)
