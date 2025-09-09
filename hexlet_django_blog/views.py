from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexPageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        },
    )


def about(request):
    return render(request, "about.html")


def page_not_found_view(request, exception):
    response = render(request, "errors/404.html")
    response.status_code = 404
    return response


def redirect(request):
    return HttpResponseRedirect(reverse("show_article", args=[2]))
