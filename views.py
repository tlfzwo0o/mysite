#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello World")

"""def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)"""

def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	#assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def display_meta(request):
	values = request.META.items()
	values.sort()
	#html = []
	#for k, v in values:
	#	html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
	#return HttpResponse('<table>%s</table>' % '\n'.join(html))
	return render_to_response('display_meta.html', {'values' : values})



