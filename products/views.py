from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Animal, Category
from .forms import ServiceForm
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
    animals = Animal.objects.order_by('animal')
    categories = Category.objects.all()

    context = {
        'service': service,
        'animals': animals,
        'categories': categories,
    }

    return render(request, 'products/service_detail.html', context)


@login_required
def add_service(request):
    """ Add a new service to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Hey, you are not authorised to be down here!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add servce, please check if form is valid')
    else:
        form = ServiceForm()
    template = 'products/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit an existing service on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Hey, you are not authorised to be down here!')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure valid form.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.service_type}')

        template = 'products/edit_service.html'
        context = {
            'form': form,
            'service': service
        }

        return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete service from site """
    if not request.user.is_superuser:
        messages.error(request, 'Hey, you are not authorised to be down here!')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service gone forever...')
    return redirect(reverse('services'))
