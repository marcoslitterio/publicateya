from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def cronograma(peticion):
	
	return render_to_response('admin/administracion/listados/cronograma.html',
                                  context_instance=RequestContext(peticion))
