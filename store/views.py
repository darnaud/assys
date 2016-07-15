from django.shortcuts import render

from .models import Item
# Create your views here.
def index(request):
	return render(request, 'template.html')

def store(request):
	count = Item.objects.all().count()

	# count will be passsed to the template
	context = {
		'count': count,
	}
	request.session['location'] = 'unknown'
	if request.user.is_authenticated():
		request.session['location'] = 'Earth'
	return render(request, 'base.html', context)