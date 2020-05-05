from django.shortcuts import render
from django.http import Http404


def Home(request):
		return("Hello world!!")

def get_url(request):
	try:
		Link = request.params.get('id')
		return redirect(Link)
	except MyModel.DoesNotExist:

		raise Http404("No MyModel matches the given query.")
