from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book

# Create your views here.http://localhost:8000/

#def search_form(request): 
#    	return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
		#message = 'You searched for: %r' % request.GET['q']
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books':books, 'query':q})
	
		#message = 'You submitted an empty form.'
		#return HttpResponse('Please submit a search term')
	return render_to_response('search_form.html', {'errors': errors})