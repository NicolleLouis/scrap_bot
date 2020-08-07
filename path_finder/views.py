from django.http import HttpResponseRedirect
from django.shortcuts import render

from path_finder.forms.url_data import UrlDataForm
from path_finder.repositories.url_data import UrlDataRepository
from path_finder.services.url_data import UrlDataService
from path_finder.services.html_content_analyser import HtmlContentAnalyserService


# Create your views here.
# ToDo split this in several file, it is filthy
def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "path_finder/home.html", context)


def analyse_url(request):
    if request.method == 'POST':
        form = UrlDataForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            UrlDataRepository.update_url(url)
            UrlDataService.save_html_content_from_url()
            return HttpResponseRedirect('/path_finder')
    else:
        form = UrlDataForm()

    context = {
        "title": "Analyse Url",
        "form": form
    }

    return render(request, 'path_finder/analyse_url.html', context)


def display_classes(request):
    context = {
        "title": "Home",
        "classes": HtmlContentAnalyserService.get_classes_with_occurences(
            UrlDataRepository.get_or_create_url_data().html_content
        )
    }
    return render(request, "path_finder/classes_from_url.html", context)
