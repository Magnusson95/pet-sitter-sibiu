from django.shortcuts import render
from products.models import Service

# Create your views here.


def index(request):
    """ A view to return the index page """

    services = Service.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'home/index.html', context)
