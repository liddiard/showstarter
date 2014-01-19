from django.views.generic.base import TemplateView

from .models import Show, Episode


class FrontView(TemplateView):

    template_name = "front.html"


class SingleShowView(TemplateView):
    
    template_name = "show_single.html"

    def get_context_data(self, **kwargs):
        context = super(SingleShowView, self).get_context_data(**kwargs)
        show = self.kwargs.get('show')
        s = Show.objects.get(pk=show)
        context['show'] = s
        episodes = Episode.objects.filter(show=s).order_by('season', 'episode')
        context['episodes'] = episodes
        return context


class ComparisonShowView(TemplateView):
    
    template_name = "show_comparison.html"

    def get_context_data(self, **kwargs):
        context = super(ComparisonShowView, self).get_context_data(**kwargs)
        return context
