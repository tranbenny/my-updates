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
	weather = findWeather()
	renderOptions = { 
		'NFbooks' : allNFBooks, 
		'Fbooks' : allFBooks, 
		'howToBooks' : howToBooks, 
		'date' : results["published_date"],
		'weather' : weather
	}
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

def findWeather():
	yahooWeatherAPI = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22seattle%2C%20wa%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
	weather = requests.get(yahooWeatherAPI)
	weatherInfo = weather.json()
	weatherResults = weatherInfo["query"]["results"]
	cityResult = weatherResults["channel"]
	dayInfo = cityResult["item"]
	return dayInfo["description"]
	# return render(request, "content/weather.html")











