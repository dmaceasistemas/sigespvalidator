from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template  import RequestContext 

from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.core.servers.basehttp import FileWrapper 
from django.conf import settings    


from SigespValidator.apps.home.forms import ValidarConstancia

import requests
import json

# Rhonal Chirinos 

def home_view(requst):
	
		return render_to_response('base.html',context_instance=RequestContext(requst))
 
def constancia_view(request):
	
		mensaje = ""
		
		if request.method =='POST' and request.is_ajax():
			form = ValidarConstancia(request.POST)
			
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				# armo la variable que le voy a pasar a sigeps 
				variable = {'codigoVerificacion':codigo}
				#url 
				#url = 'http://172.16.0.31/sno/class_folder/sigesp_espc_verifica_constancia_personal.php'
				
				url = 'http://sigesp.cvapedrocamejo.gob.ve/sno/class_folder/sigesp_espc_verifica_constancia_personal.php'
			
				r = requests.get(url,params=variable)
			
				if r.status_code == 200:

					if len(r.json()) == 0:
						respuesta = json.dumps({'msj':'Codigo Invalido !! ','codigo':'404'})
					else:
						respuesta = json.dumps(r.json())
						# si es tipo 3 es por que el personal esta Egresado de la Empresa

					return HttpResponse(respuesta,mimetype='application/json')				
				else:
			
					respuesta = json.dumps({'msj':'Error al Intentar Realizar la Operacion '})
					return HttpResponse(respuesta,mimetype='application/json')
			
			else:
				respuesta = json.dumps({'msj':'Codigo Invalido !! ','codigo':'404'})
				return HttpResponse(respuesta,mimetype='application/json')
		
		elif request.method == 'GET':
			form = ValidarConstancia()
		
		ctx ={'form':form,'msj':mensaje}
		
		return render_to_response('Sigep/validarConstancia.html',ctx,context_instance=RequestContext(request))
 

 
