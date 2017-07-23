from django.contrib import admin
from django.utils.html import format_html
from url_shortener.models import URLShortcut


class URLShortcutAdmin(admin.ModelAdmin):
    list_display = ["slug", "linked_url"]
    list_display_links = ['slug', ]

    def linked_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)
    linked_url.short_description = "URL"

    class Meta:
        model = URLShortcut

admin.site.register(URLShortcut, URLShortcutAdmin)
