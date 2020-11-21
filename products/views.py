from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)


def service_detail(request, service_id):
    """ A view to show details of a specific service """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'products/service_detail.html', context)
