from django.shortcuts import render

# Create your views here.


def content(request):
 return render(request, 'info_box/info.html')
