from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	# return HttpResponse("HELLO WORLD !")
	context = {}
	context['hello'] = 'HELLO WORLD !'
	return render(request, 'hello.html', context)