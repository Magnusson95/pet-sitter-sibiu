from django.shortcuts import render
from collage.models import Collage
# Create your views here.


def view_collage(request):
    """ A view to return the collage page """
    photos = Collage.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, 'collage/collage.html', context)
