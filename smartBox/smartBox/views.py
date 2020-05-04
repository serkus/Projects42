from django.shortcuts import render , redirect
from django.http import HttpResponse
from taskList.models import TaskList
from django.http import Http404



def Home(request):
		return(HttpResponse("Hello world!!"))

def get_url(request):
#	Path = request.path
#	Id_link = Path..split('/')
	try:
		Link = request.params.get('id')
		return redirect(Link)
	except MyModel.DoesNotExist:

		raise Http404("No MyModel matches the given query.")


