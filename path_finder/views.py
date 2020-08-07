from django.http import HttpResponseRedirect
from django.shortcuts import render

from path_finder.forms.url_data import UrlDataForm
from path_finder.repositories.url_data import UrlDataRepository


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
            return HttpResponseRedirect('/path_finder')
    else:
        form = UrlDataForm()

    context = {
        "title": "Analyse Url",
        "form": form
    }

    return render(request, 'path_finder/analyse_url.html', context)
