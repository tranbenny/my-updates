from django.shortcuts import get_object_or_404, render
import requests
import json


# Create your views here.
def list(request):
	nyTimesAPI = "http://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=8340b1a97466c874731b753cd607a32e%3A7%3A72549146"
	titles = requests.get(nyTimesAPI)
	info = titles.json()
	results = info["results"]
	listOfBestSellers = results["lists"] #array
	allBooks = []
	for lists in listOfBestSellers: 
		if (lists["list_name"] == "Combined Print and E-Book Nonfiction"):
			allBooks = lists["books"]
			break	
	renderOptions = { 'books' : allBooks, 'date' : results["published_date"]}
	return render(request, "content/update_list.html", renderOptions)