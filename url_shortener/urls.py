from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'skrot/(?P<slug>\w+)/$',
        views.GeneratedShortcutView.as_view(),
        name='generated-shortcut'),
    url(r'(?P<slug>\w+)/$',
        views.ShortcutView.as_view(),
        name='shortcut'),
    url(r'$',
        views.GenerateShortcutView.as_view(),
        name='generate-shortcut'),
]
