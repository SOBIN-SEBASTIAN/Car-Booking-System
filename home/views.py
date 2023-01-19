from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

from.form import BookingForm
from.models import Cars,cartype as cartype2
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST) 
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form = BookingForm() 
    dict_form={'form':form}
    return render(request,'booking.html',dict_form)
def cars(request):
    dict_cars={
        'car':Cars.objects.all(),
    }
    return render(request,'cars.html',dict_cars)
def contact(request):
    return render(request,'contact.html')
def cartype(request):
    dict_ctype={ 
        'ctype': cartype2.objects.all(),
    }
    return render(request,'cartype.html',dict_ctype)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,'register.html', context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render (request,'booking.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,'login.html', context={"login_form":form})