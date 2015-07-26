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
	allNFBooks = []
	allFBooks = []
	howToBooks = []
	for lists in listOfBestSellers: 
		if (lists["list_name"] == "Combined Print and E-Book Fiction"):
			allFBooks = lists["books"]
		elif (lists["list_name"] == "Combined Print and E-Book Nonfiction"):
			allNFBooks = lists["books"]
		elif (lists["list_name"] == "Advice How-To and Miscellaneous"):
			howToBooks = lists["books"]
			break
	manipulateTitle(allNFBooks)	
	manipulateTitle(allFBooks)
	manipulateTitle(howToBooks)	
	renderOptions = { 'NFbooks' : allNFBooks, 'Fbooks' : allFBooks, 'howToBooks' : howToBooks, 'date' : results["published_date"]}
	return render(request, "content/update_list.html", renderOptions)


def manipulateTitle(books):
	# books is an array of dictionary objects
	for book in books: 
		title = book["title"]
		if (not title.istitle()):
			book["title"] = fixCapitals(title)

def fixCapitals(title):
	lowerCaseTitle = title.lower()
	words = lowerCaseTitle.split()
	result = ""
	for word in words:
		word = word.capitalize()
		result += word + " "
	return result.rstrip()
