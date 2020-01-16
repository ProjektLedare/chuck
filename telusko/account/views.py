from django.shortcuts import render
from django.http import HttpResponse
from .models import Homeobjects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def login(request):

#	home = Homeobjects.objects.all()
#	paginator = Paginator(home, 2)
#	page = request.GET.get('page')
#
#	try:
#		items = paginator.page(page)
#	except PageNotAnInteger:
#		items = paginator.page(1)
#	except EmptyPage:
#		items = paginator.page(paginator.num_pages)
#
#	index = items.number-1
#	max_index = len(paginator.page_range)
#	start_index = index-5 if index >= 5 else 0
#	end_index = index +5 if index <= max_index-5 else max_index
#	page_range = paginator.page_range[start_index:end_index]
#
#	context = {
#		'homes':home,
#		'items': items,
#		'page_range': page_range,
#	}
	# home = paginator.get_page(page)

	#return render(request, 'login.html', context)
	return render(request, 'login.html')

def ren(request):
	return render(request, 'pano80A_1003.htm')