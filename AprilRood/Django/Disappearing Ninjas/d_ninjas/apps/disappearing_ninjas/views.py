from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "disappearing_ninjas/index.html")

def show(request, color): 
	context = {
		"color": color
	}
	if color.lower() == "blue" or color.lower() == "red" or color.lower() == "orange" or color.lower() == "purple":
		return render(request, "disappearing_ninjas/show.html", context)
	else:
		return render(request, "disappearing_ninjas/megan.html")

def all_ninjas(request):

	return render(request, "disappearing_ninjas/all_ninjas.html")
