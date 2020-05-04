from django.shortcuts import render
from django.shortcuts import redirect
from taskList.models import TaskList
from django.http import Http404

def get_url(request):
#	Path = request.path
#	Id_link = Path..split('/')
	try:
		Link = request.params.get('id')
		return redirect(Link)
	except MyModel.DoesNotExist:

		raise Http404("No MyModel matches the given query.")

