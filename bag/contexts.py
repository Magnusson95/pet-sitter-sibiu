from django.shortcuts import get_object_or_404
from products.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        service = get_object_or_404(Service, pk=item_id)
        for animal, quantity in item_data['items_by_animal'].items():
            total += quantity * service.cost
            service_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'service': service,
                'animal': animal,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
    }

    return context
