from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

def pickPage(request, pageID):
    
    pagina = Pages.objects.get(id=pageID)
    
    
    respuesta = 'La pagina "' + pagina.name + '" dice: ' + pagina.page
    return HttpResponse(respuesta)
    
