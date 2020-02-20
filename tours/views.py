from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.utils import translation

from .models import Tour, TourType

def home(request):
    tours = Tour.objects.all()
    return render(request, 'home.html', {'tours': tours})

def tours(request):
    currentlanguage = translation.get_language_from_request(request)
    translation.activate(currentlanguage)
    request.LANGUAGE_CODE = translation.get_language()
    print(request.LANGUAGE_CODE)
    queryset = Tour.objects.filter(language = request.LANGUAGE_CODE).order_by('-last_updated')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)

    try:
        tours = paginator.page(page)
    except PageNotAnInteger:
        tours = paginator.page(1)
    except EmptyPage:
        tours = paginator.page(paginator.num_pages)

    return render(request, 'tours.html', {'tours': tours})

class TourListView(ListView):
    context_object_name = 'tours'
    template_name = 'tours.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TourListView, self).get_context_data(**kwargs)
        context['tours'] = Tour.objects.filter(language = translation.get_language()).order_by('-last_updated')
        paginator = Paginator(context['tours'], 5)
        page = self.request.GET.get('page', 1)
        
        try:
            context['tours']= paginator.page(page)
        except PageNotAnInteger:
            context['tours'] = paginator.page(1)
        except EmptyPage:
            context['tours'] = paginator.page(paginator.num_pages)

        context['types'] = TourType.objects.filter(language = translation.get_language())
        return context

    def get_queryset(self):
        queryset = Tour.objects.filter(language = translation.get_language()).order_by('-last_updated')
        return queryset

def tour(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        raise Http404
    return render(request, 'tour.html', {'tour': tour})


