from django.views.generic import View
from django.shortcuts import render

# Es la vista que permite tener mas contro.
# Vistas de clases y vistas de funiones.


class HomeView(View):
    def get(self, request, *args , **kwargs):
        contex  ={
            
        }
        return render(request, 'index.html', contex)
# Get requested es lo que pide la informacion para ver
# Post request es lo que tu envias al servidor.