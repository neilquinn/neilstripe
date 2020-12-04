from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World")

def simpleCheckout(request):
	return HttpsResponse("simple checkout page")

def paymentIntent(request):
	return HttpsResponse("payment intent page")