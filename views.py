from django.http import HttpResponse

def index(request)
	return HttpResponse("hello!reader.")
def login(request)
	return redirect("/index")
