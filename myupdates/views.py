from django.shortcuts import render

def load_home(request):
	return render(request,'index.html')