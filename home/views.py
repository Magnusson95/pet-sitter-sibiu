from django.shortcuts import render
from products.models import Service
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from reviews.models import UserReview
from .models import EmailForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    if request == "POST":
        services = Service.objects.all()
        reviews = UserReview.objects.all()
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        email_form = EmailForm(form_data)

        email = email_form.save()
        customer_email = email.email
        subject = 'Thank you for emailing us'
        body = email.message

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

        context = {
            'services': services,
            'reviews': reviews,
            'email_form': email_form,
        }
        messages.success('Your email has been sent')
        return render(request, 'home/index.html', context)

    else:
        services = Service.objects.all()
        reviews = UserReview.objects.all()
        form_data = {
            'name': 'name',
            'email': 'email',
            'message': 'message',
        }
        email_form = EmailForm(form_data)

        context = {
            'services': services,
            'reviews': reviews,
            'email_form': email_form,
        }
        return render(request, 'home/index.html', context)
