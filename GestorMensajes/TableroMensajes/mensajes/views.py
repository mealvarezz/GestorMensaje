from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    usuario = request.user
    mensajes = Mensaje.objects.filter(destinatario=usuario)
    return render(request, 'vista.html', {'mensajes': mensajes})
