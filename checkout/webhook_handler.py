from django.http import HttpResponse


class StripeWH_Handler:
    """"Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic webhook event
        """
        return HttpResponse(
            content=f'Generic webhook received from stripe: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook event
        """
        return HttpResponse(
            content=f'Webhook received from stripe: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a failed payment_intent webhook event
        """
        return HttpResponse(
            content=f'Webhook received from stripe: {event["type"]}',
            status=200)
