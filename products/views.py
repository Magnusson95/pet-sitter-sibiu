from django.shortcuts import render
from .models import Service

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)


def service_detail(request):
    """ A view to show details of a specific service """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'products/services_detail.html', context)
