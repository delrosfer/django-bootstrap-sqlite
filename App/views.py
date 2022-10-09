from django.shortcuts import render
from App.models import Contact
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

#imports para login y logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Funcion para renderiza homepage
@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)


def home(request):
	contact_list = Contact.objects.all().order_by('-created_at')
	return render(request, 'home.html', {"contacts":contact_list})


#def employee_json(request):
#	contacts = Contact.objects.all()
#	data = [contact.get_data() for contact in contacts]
#	response = {'data': data}
#	return JsonResponse(response)

def add_contact(request):
	if request.method=="POST":
		if request.POST.get('name') \
			and request.POST.get('email') \
			and request.POST.get('occupation') \
			and request.POST.get('salary') \
			and request.POST.get('gender') \
			or request.POST.get('note'):
			contact = Contact()
			contact.name = request.POST.get('name')
			contact.email = request.POST.get('email')
			contact.occupation = request.POST.get('occupation')
			contact.salary = request.POST.get('salary')
			contact.gender = request.POST.get('gender')
			contact.note = request.POST.get('note')
			contact.save()
			messages.success(request, "Se agregó el contacto exitosamente!!")
			return HttpResponseRedirect("/")
	else:
			return render(request, 'add.html')

def contact(request, contact_id):
	contact = Contact.objects.get(id = contact_id)
	if contact != None:
		return render(request, "edit.html", {'contact':contact})

def edit_contact(request):
	if request.method=="POST":
		contact = Contact.objects.get(id = request.POST.get('id'))
		if contact != None:
			contact.name = request.POST.get('name')
			contact.email = request.POST.get('email')
			contact.occupation = request.POST.get('occupation')
			contact.salary = request.POST.get('salary')
			contact.gender = request.POST.get('gender')
			contact.note = request.POST.get('note')
			contact.save()
			messages.success(request, "Se actualizó el contacto exitosamente!!")
			return HttpResponseRedirect("/")

def delete_contact(request, contact_id):
	contact = Contact.objects.get(id = contact_id)
	contact.delete()
	messages.success(request, "Se eliminó el contacto exitosamente!!")
	return HttpResponseRedirect("/")

#funcion para login
def Login(request):
	if request.user == None or request.user == "" or request.user.username == "":
		return render(request, "login.html")
	else:
		return HttpResponseRedirect('/')

#funcion para login user
def LoginUser(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user != None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			messages.error(request, "Ingresa tus datos correctamente.!!")
			return HttpResponseRedirect('/')

#funcion para logout
def LogoutUser(request):
	logout(request)
	request.user = None
	return HttpResponseRedirect('/')