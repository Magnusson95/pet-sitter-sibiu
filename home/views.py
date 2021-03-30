from django.shortcuts import render
from products.models import Service
from reviews.models import UserReview

# Create your views here.


def index(request):
    """ A view to return the index page """

    services = Service.objects.all()
    reviews = UserReview.objects.all()

    context = {
        'services': services,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)
