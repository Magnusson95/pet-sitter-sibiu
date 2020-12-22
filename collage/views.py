from django.shortcuts import render
from django.core.paginator import Paginator
from collage.models import Collage
# Create your views here.


def view_collage(request):
    """ A view to return the collage page """
    photos = Collage.objects.all()

    photo_paginator = Paginator(photos, 20)

    page_num = request.GET.get('page')

    page = photo_paginator.get_page(page_num)

    context = {
        'count': photo_paginator.count,
        'page': page
    }
    return render(request, 'collage/collage.html', context)
