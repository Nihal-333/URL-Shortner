from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LongToShort
# Create your views here.
def hello_world(request):
	return HttpResponse("Hello world!")


def home_page(request):

	context={
		"submitted": False,
		"error" : False
	}
	
	if request.method=='POST':
		#print(request.data)
		data=request.POST
		long_url=data['longurl']
		custom_name=data['custom_name']
		
		print(long_url)
		print(custom_name)

		#CREATE
		try: 
			obj = LongToShort(Long_url=long_url, Short_url=custom_name)
			obj.save()
			#READ
			DATE = obj.Date
			CLICKS = obj.Clicks

			context["long_url"] = long_url
			context["short_url"] = request.build_absolute_uri() + custom_name
			context["date"] = DATE
			context["clicks"] = CLICKS
			context["submitted"] = True

		except:
			context["error"] = True

	else:
		print("User not sending any data")

	
	return render(request, "index.html",context)

def redirect_url(request, ShortURL):
	row = LongToShort.objects.filter(Short_url=ShortURL)
	print(row)
	if len(row) == 0:
		return HttpResponse("No such short url exist")

	obj=row[0]
	long_url = obj.Long_url

	# return HttpResponse(long_url)

	obj.Clicks = obj.Clicks + 1
	obj.save()

	return redirect(long_url)


def all_analytics(request):

	rows = LongToShort.objects.all()

	context = {
		"rows": rows
	}

	return render(request, "all-analytics.html", context)


def task(request):
	context={
		"my_name": "Nihal",
		"x": 10
	}
	return render(request,"task.html",context)

