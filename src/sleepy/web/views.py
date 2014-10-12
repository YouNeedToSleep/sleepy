from django.views.generic import TemplateView


class IndexView(TemplateView):
    """View for the index page"""
    template_name = 'sleepy/web/index.html'
