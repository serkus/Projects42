from django.shortcuts import render
from django.shortcuts import redirect
from taskList.models import TaskList
from django.http import Http404

def get_url(request):
#	Path = request.path
#	Id_link = Path..split('/')
	try:
		Link = request.params.get('id')
		add_click(request)
		return redirect(Link)
	except MyModel.DoesNotExist:

		raise Http404("No MyModel matches the given query.")
"""
def  add_click(url):
	TaskList.objects.remove(++)
"""
def get_statictic(request):
	pass

def get_actions(request):
	pass

