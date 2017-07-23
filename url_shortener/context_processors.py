from django.contrib.sites.models import Site


def current_domain(request):
    """
    :param request:
    :return: context for template with current domain (from django sites)
    """
    current_site = Site.objects.get_current()
    return {'CURRENT_DOMAIN': current_site.domain}
