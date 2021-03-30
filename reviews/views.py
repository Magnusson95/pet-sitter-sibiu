from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from profiles.models import UserProfile


@login_required
def review(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add review, please check if form is valid')
    else:
        form = ReviewForm(instance=profile)
    template = 'reviews/review.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
