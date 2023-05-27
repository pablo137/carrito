from django.shortcuts import render 
from django.views import View

def perfil(request):
    return render(request,'perfil.html')


class PerfilView(View):

    pass