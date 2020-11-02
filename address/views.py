from django.shortcuts import render, redirect
from .models import Country, City
from .forms import CountryForm, CityForm
# Create your views here.
def create_country(request):
	form=CountryForm()
	if request.method=='POST':
		form=CountryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_country')
	else:
		countries=Country.objects.all()
		context={'form':form, 'countries':countries}
		return render(request, 'address/country.html', context)
def edit_country(request, id):
	country=Country.objects.get(id=id)
	form=CountryForm(instance=country)
	if request.method=='POST':
		form=CountryForm(request.POST, instance=country)
		if form.is_valid():
			form.save()
			return redirect('create_country')
	else:
		context={'form':form}
		return render(request, 'address/edit_country.html', context)
def delete_country(request, id):
	country=Country.objects.get(id=id)
	country.delete()
	return redirect('create_country')
def create_city(request):
	form=CityForm()
	if request.method=='POST':
		form=CityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_city')
	else:
		cities=City.objects.all()
		context={'form':form, 'cities':cities}
		return render(request, 'address/city.html', context)
def edit_city(request, id):
	city=City.objects.get(id=id)
	form=CityForm(instance=city)
	if request.method=='POST':
		form=CityForm(request.POST, instance=city)
		if form.is_valid():
			form.save()
			return redirect('create_city')
	else:
		context={'form':form}
		return render(request, 'address/edit_city.html', context)
def delete_city(request, id):
	city=City.objects.get(id=id)
	city.delete()
	return redirect('create_city')