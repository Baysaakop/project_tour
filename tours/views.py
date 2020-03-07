from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.utils import translation

from .models import Tour, TourType, TourReview

def home(request):
    carousel_tours = Tour.objects.all()[:5]
    suggested_tours = Tour.objects.all()[:3]
    context = {
        'carousel_tours': carousel_tours,
        'suggested_tours': suggested_tours
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def tours(request):
    currentlanguage = translation.get_language_from_request(request)
    translation.activate(currentlanguage)
    request.LANGUAGE_CODE = translation.get_language()
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
    suggested_tours = Tour.objects.all().order_by('views')[:3]
    tour = Tour.objects.get(pk=pk)
    tour.views += 1       
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']                
        comment = request.POST['comment']
        is_liked = request.POST.get('like', False)
        rating = request.POST.get('rating', False)
        if is_liked != False:
            is_liked = True
            tour.likes += 1
        tourreview = TourReview.objects.create(            
            username = username,
            email = email,
            comment = comment,
            is_liked = is_liked,
            rating = rating,
            tour = tour,
        )

    tour.save() 
    tourreviews = TourReview.objects.filter(tour=tour).order_by('-updated_at')
    context = {
        'suggested_tours': suggested_tours,
        'tour': tour,
        'tourreviews': tourreviews
    }
    return render(request, 'tour.html', context)

def touredit(request):
    tours = Tour.objects.all()
    target = None
    if request.method == 'GET':
        tourname = request.GET.get('tourname')
        target = Tour.objects.filter(name=tourname).first()
    elif request.method == 'POST':
        pk = request.POST.get('pk', False)
        target = Tour.objects.get(pk=pk)
        target.name = request.POST['name']
        target.description = request.POST['description']
        target.duration = request.POST['duration']
        target.includes = request.POST['included']
        target.notincludes = request.POST['notincluded']
        target.views = request.POST['views']
        target.likes = request.POST['likes']
        target.rating = request.POST['rating']
        target.save()

    context = {
        'tours': tours,
        'target': target
    }
    return render(request, 'touredit.html', context)

def touradd(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        duration = request.POST['duration']
        includes = request.POST['included']
        notincludes = request.POST['notincluded']
        views = request.POST['views']
        likes = request.POST['likes']
        rating = request.POST['rating']
        tour = Tour.objects.create(
            name = name,
            description = description,
            duration = duration,
            includes = includes,
            notincludes = notincludes,
            views = views,
            likes = likes,
            rating = rating
        )

        return redirect('tour_edit')

    return render(request, 'touradd.html')


