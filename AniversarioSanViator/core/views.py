from django.shortcuts import render, HttpResponse

contenido_html="""
<h1>Menú navegación</h1>
<ul>
    <li><a href="/">Índice</a></li>
    <li><a href="/contacto">Contacto</a></li>
    <li><a href="/noticias">Noticias</a></li>
    <li><a href="/acerca">Acerca de</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def contacto(request):
    return render(request,'core/contacto.html')

def acerca(request):
    return render(request,'core/acerca.html')