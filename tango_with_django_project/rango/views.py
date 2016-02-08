from django.shortcuts import render
from rango.models import Category
# from django.http import HttpResponse

# Create your views here.
	
def index(request):

	#Creates a dictionary to pass the to the template engine as the context from index.html
	#boldmessage' is the same as {{ boldmessage }} from index.html template
	#In this scenario 'boldmessage' is mapped to the string "I am bold font from the context" and the string
	#will replace any instance of 'boldmessage' in a rendered response
	context_dict = {'boldmessage': "I am bold font from the context"}

	#Returns a rendered response to the client
	#Request is the user's request
	#The second parameter is the location of the template we want to use, with context_dict being 
	#the dictionary above
	return render(request, 'rango/index.html', context_dict)