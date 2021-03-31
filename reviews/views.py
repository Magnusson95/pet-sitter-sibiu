from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from profiles.models import UserProfile
from .models import UserReview


@login_required
def review(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if UserReview.objects.filter(user=request.user).exists():
            messages.error(request, 'You have already posted a review, greedy...')
            return redirect('home')
        else:
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
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
