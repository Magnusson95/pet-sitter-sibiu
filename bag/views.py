from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Service, Animal, Category
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a service to the bag """

    service = Service.objects.get(pk=item_id)
    animal = request.POST['animal_selector']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if animal:
        if item_id in list(bag.keys()):
            if animal in bag[item_id]['items_by_animal'].keys():
                bag[item_id]['items_by_animal'][animal] += quantity
                messages.info(request, f'We have added another {quantity} {service.service_type}s for your {animal}')
            else:
                bag[item_id]['items_by_animal'][animal] = quantity
                messages.success(request, f'We have added {quantity} {service.service_type}s for your {animal}')
        else:
            bag[item_id] = {'items_by_animal': {animal: quantity}}
            messages.success(request, f'We have added {quantity} {service.service_type}s for your {animal}')
    else:
        messages.error(request, 'Please select an animal')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a product in the bag """

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    animal = request.POST['animal_selector']
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id]['items_by_animal'][animal] = quantity
        messages.warning(request, f'We have updated {service.service_type} quantity to {bag[item_id]}')
    else:
        del bag[item_id]['items_by_animal'][animal]
        if not bag[item_id]['items_by_animal'][animal]:
            bag.pop(item_id)
            messages.warning(request, f'We have removed {service.service_type} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove a product from the bag """

    try:
        service = Service.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.warning(request, f'We have removed {service.service_type} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
