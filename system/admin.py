from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import admin
from django.urls import path
from django import forms

from .views.signup import InviteView
from .views.bot import CreateBotView
from .models import User


class AdvancedUserChangeForm(UserChangeForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'vTextField'}),
            'wikidot_username': forms.TextInput(attrs={'class': 'vTextField'})
        }


@admin.register(User)
class AdvancedUserAdmin(UserAdmin):
    form = AdvancedUserChangeForm

    list_display = ['username_or_wd', 'email']
    search_fields = ['username', 'wikidot_username', 'email']
    readonly_fields = ["api_key"]

    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] += ("bio", "avatar")
    fieldsets[0][1]["fields"] += ("type", "wikidot_username", "api_key")

    inlines = []

    def get_urls(self):
        urls = super(AdvancedUserAdmin, self).get_urls()
        urls.insert(0, path("invite/", InviteView.as_view()))
        urls.insert(0, path("newbot/", CreateBotView.as_view()))
        urls.insert(0, path("<id>/activate/", InviteView.as_view()))
        return urls

    def username_or_wd(self, obj):
        if obj.type == User.UserType.Wikidot:
            return 'wd:%s' % obj.wikidot_username
        return obj.username

    def get_form(self, request, *args, **kwargs):
        form = super().get_form(request, *args, **kwargs)
        if 'wikidot_username' in form.base_fields:
            form.base_fields['wikidot_username'].required = False
        return form
