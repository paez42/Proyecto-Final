from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView , ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models.query import QuerySet

from . import forms, models


def home(request):    
    return render(request,"turno/index.html")

# ********  TURNO LUGAR *************************

#LIST

class TurnoLugarList(ListView):
    model = models.TurnoLugar
    
    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.TurnoLugar.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.TurnoLugar.objects.all()
        return object_list

#CREATE

class TurnoLugarCreate(CreateView):
    model = models.TurnoLugar
    form_class = forms.TurnoLugarForm
    success_url = reverse_lazy("turno:home")  #<-- Para redireccionar despues de guardar o realizar una accion

#UPDATE

class TurnoLugarUpdate(UpdateView):
    model = models.TurnoLugar
    form_class = forms.TurnoLugarForm
    success_url = reverse_lazy("turno:turnolugar_list")

#DETAIL

class TurnoLugarDetail(DetailView):
    model = models.TurnoLugar

#DELETE

class TurnoLugarDelete(LoginRequiredMixin, DeleteView):
    model = models.TurnoLugar
    success_url = reverse_lazy("turno:turnolugar_list")
    

# ********  TURNO *************************

class TurnoList(ListView):
    model = models.Turno
    
    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Turno.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Turno.objects.all()
        return object_list

#CREATE

class TurnoCreate(CreateView):
    model = models.Turno
    form_class = forms.TurnoForm
    success_url = reverse_lazy("turno:home")  #<-- Para redireccionar despues de guardar o realizar una accion

#UPDATE

class TurnoUpdate(UpdateView):
    model = models.Turno
    form_class = forms.TurnoForm
    success_url = reverse_lazy("turno:turno_list")

#DETAIL

class TurnoDetail(DetailView):
    model = models.Turno

#DELETE

class TurnoDelete(LoginRequiredMixin, DeleteView):
    model = models.Turno
    success_url = reverse_lazy("turno:turno_list")