from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import ListView
from django.utils import translation
from django.contrib.auth.models import User
from datetime import datetime

from .models import Tour, TourType, TourImage, Price, Itinerary, TourComment, TourLike, TourRating

def home(request):
    carousel_tours = Tour.objects.all()[:5]
    suggested_tours = Tour.objects.all()[:3]
    images = TourImage.objects.all()
    prices = Price.objects.all()
    context = {
        'carousel_tours': carousel_tours,
        'suggested_tours': suggested_tours,
        'images': images,
        'prices': prices
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

class TourListView(ListView):
    context_object_name = 'tours'
    template_name = 'tourlist.html'
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
        context['images'] = TourImage.objects.all()
        context['prices'] = Price.objects.all()
        return context

    def get_queryset(self):
        queryset = Tour.objects.filter(language = translation.get_language()).order_by('-last_updated')
        return queryset

def getTourRating(tour_id):
    tour = Tour.objects.get(pk=tour_id)
    ratings = TourRating.objects.filter(tour=tour)
    count = ratings.count()
    average = 0
    if count > 0:
        sum = 0
        for r in ratings:
            sum += r.rating
        average = sum / count
    return average

def tour(request, pk):    
    tour = Tour.objects.get(pk=pk)
    tour.views += 1           
    tour.save() 
    tour_image = TourImage.objects.filter(tour=tour).first()
    tour_itineraries = Itinerary.objects.filter(tour=tour)    
    tour_comments = TourComment.objects.filter(tour=tour).order_by('-updated_at') 
    tour_like = None
    tour_rating = None

    if request.user.is_authenticated:
        tour_like = TourLike.objects.filter(tour=tour, user=request.user).first()
        tour_rating = TourRating.objects.filter(tour=tour, user=request.user).first()   

    likes = 0
    likes = TourLike.objects.filter(tour=tour, is_liked=True).count()    
    rating_count = TourRating.objects.filter(tour=tour).count()
    rating = getTourRating(pk)
    suggested_tours = Tour.objects.all().order_by('views')[:3]
    prices = Price.objects.all()  
    images = TourImage.objects.all()      

    context = {        
        'tour': tour,
        'tour_image': tour_image,
        'tour_itineraries': tour_itineraries,
        'tour_like': tour_like,
        'tour_rating': tour_rating,
        'tour_comments': tour_comments,
        'likes': likes,
        'rating': rating,
        'rating_count': rating_count,
        'suggested_tours': suggested_tours,
        'prices': prices,        
        'images': images
    }
    return render(request, 'tour.html', context)

@login_required
def likeTour(request):
    if request.method == 'GET':
        tour_id = request.GET.get('tour_id')
        tour = Tour.objects.get(pk=tour_id)
        result = TourLike.objects.filter(tour=tour, user=request.user).first()
        if result is None:
            result = TourLike.objects.create(
                tour = tour,
                user = request.user,
                is_liked = True,
            )
        else:
            if result.is_liked:
                result.is_liked = False
            else:
                result.is_liked = True
            result.save()

        data = {
            'is_liked':  result.is_liked
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Request method is not a GET")

@login_required
def rateTour(request):
    if request.method == 'GET':        
        tour_id = request.GET.get('tour_id')
        tour = Tour.objects.get(pk=tour_id)
        rating = request.GET.get('rating')
        result = TourRating.objects.filter(tour=tour, user=request.user).first()                    
        if result is None:   
            result = TourRating.objects.create (                
                tour = tour,            
                user = request.user,   
                rating = rating
            )                                           
        else: 
            result.rating = rating
            result.save()   

        count = TourRating.objects.filter(tour=tour).count()
        average = getTourRating(tour_id)
        data = {
            'count': count,
            'average':  average
        }
        return JsonResponse(data)                       
    else:
        return HttpResponse("Request method is not a GET") 

@login_required
def commentTour(request):
    if request.method == 'GET':
        tour_id = request.GET.get('tour_id')
        tour = Tour.objects.get(pk=tour_id)
        comment = request.GET.get('comment')    
        result = TourComment.objects.create(
            user = request.user,
            tour = tour,
            comment = comment
        )
        rating = 0
        tour_rating = TourRating.objects.filter(tour=tour, user=request.user)
        if tour_rating is not None:
            rating = tour_rating.first().rating
        data = {
            'username': result.user.username,
            'comment':  result.comment,
            'updated_at': result.updated_at.strftime('%B %d, %Y'),
            'rating': rating
        }
        return JsonResponse(data) # Sending an success response
    else:
        return HttpResponse("Request method is not a GET") 

@login_required
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

        return redirect('tourlist')

    return render(request, 'touradd.html')


