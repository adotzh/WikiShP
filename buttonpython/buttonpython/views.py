from django.shortcuts import render
import requests
from . import wiki
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Case


def button(request):
	return render(request, 'home.html')

def calc(request):
	param1 = request.POST.get('param1')
	param2 = request.POST.get('param2')
	out = wiki.ShortestPath(param1,param2)
	if isinstance(out, list):
		path = "-->".join(out)
		return render(request, 'home.html', {'shortest_path': path})
  
class IndexView(generic.ListView):
    template_name = 'templates/home.html'
    context_object_name = 'case_list'
  
    def get_queryset(self):
        return Case.objects.all()
