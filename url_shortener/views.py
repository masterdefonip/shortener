from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect

from .models import URLShortcut


class GenerateShortcutView(CreateView):
    """
    Creating shortcut for given URL
    """
    model = URLShortcut
    fields = ['url', ]
    template_name = 'generate_shortcut.html'

    def form_valid(self, form):
        form.save()
        return self.get_success_url(form.instance.slug)

    def get_success_url(self, slug):
        return redirect(reverse('generated-shortcut', kwargs={'slug': slug}))


class GeneratedShortcutView(DetailView):
    """
    View after created shortcut
    """
    model = URLShortcut
    template_name = 'generated_shortcut.html'


class ShortcutView(DetailView):
    """
    View for shortcut with redirect to given URL
    """
    model = URLShortcut

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return redirect(self.object.url)
