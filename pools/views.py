# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from pools.models import *

# Django libs
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseNotAllowed
from django.db.models import Q, Avg, Sum, Count
from django.utils import simplejson
from django.core import serializers
from django.db.models.signals import post_save
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.conf import settings
from django.utils.timezone import utc

def index(request):
    return HttpResponse("Hello, world. You're at the pools index.")

def detail(request, quiniela_id):
    return HttpResponse("You're looking at pool %s." % quiniela_id)

def ingresar(request):
    return HttpResponse("You're looking at the results of poll. ")

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def ingresar(request):
	print "ingresar"
	if request.user.is_authenticated() :
		return redirect('/home',request)
	next = request.GET.get('next',None)
	if next:
		return render_to_response('pools/ingresar.html',{'next':next}, RequestContext(request))
	return render_to_response('pools/ingresar.html', RequestContext(request))

def login_call(request):
	message = 'Usuario ya se encuentra conectado'
	if request.user is not None:
		name = request.POST.get('login',None)
		user = authenticate(username = name, password=request.POST.get('password',None))
		print 'PAPAPAPÁ'
		if user is not None:
			if user.is_active:
				message = "¡Se ha iniciado sesión!"
				login(request, user)
				#Si desea recordar sesión, cambia el tiempo de expiración a una fecha definida en REMEBER_SESSION_TIME en settings.py
				if request.POST.get('remember_me', False):
					request.session['remember_me']=True
					request.session.set_expiry(settings.REMEMBER_SESSION_TIME)
				groups = set(user.groups.values_list('name',flat=True))
				#profile = user.get_profile()
				next = request.POST.get('next',None)
				if next:
					return redirect(next,request,message)
				if u'REGULAR' in groups:
					return redirect('/pools',request,message)
				elif u'ADMINISTRADOR' in groups:
					return redirect('/pools',request,message)
				else :
					return redirect('/pools',request,message)
			else:
				messages.info(request, '¡Su usuario ha sido deshabilitado!')
				#message = "¡Su usuario ha sido deshabilitado!"
				return redirect('/pools/ingresar',request)
		else:
			messages.info(request, 'Usuario y/o contraseña incorrectos.')
			#message = "Usuario y/o contraseña incorrectos."
			return redirect('/pools/ingresar',request)
	else:
		message = request.user.username
	#return render_to_response('audit/index.html', {'message': message},RequestContext(request))
	return redirect('/pools',request)

def logout_call(request):
	message = 'No ha iniciado sesión en el sistema!'
	if request.user is not None:
		message = 'Se ha cerrado la sesión'
		logout(request)
	#return render_to_response('audit/index.html', {'message': message})
	return redirect('/',request, message)	
