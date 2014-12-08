from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from mysite.books.models import Book
from django.core.mail import send_mail
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

def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a sugject')
		if not request.POST.get('message',''):
			errors.append('Enter a message')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			send_mail(
					request.POST['subject'],
					request.POST['message'],
					request.POST.get('email', '93977842@qq.com'),
					['tlfzwo0o@163.com'],
				)
			return HttpResponseRedirect('/contact/thanks/')
	
	return render_to_response('contact_form.html', {'errors':errors})		
