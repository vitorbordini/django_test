from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Paciente
from .forms import PacienteForm
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class IndexView(generic.TemplateView):
    model = Paciente
    template_name = 'pacientes/index.html'
    def get_queryset(self):
        pass

class AddView(generic.TemplateView):
    model = Paciente
    template_name = 'pacientes/adicionar.html'


class ExcluirView(generic.TemplateView):
    model = Paciente
    template_name = 'pacientes/excluir.html'

class ResultsView(generic.ListView):
    lista_pacientes = Paciente.objects.all()
    template_name = 'pacientes/results.html'
    context_object_name = 'todos_os_pacientes'
    def get_queryset(self):
        return self.lista_pacientes


def add(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = PacienteForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
                nome = form['name'].value()
                data = form['data'].value()
                tipo = form['tipo'].value()
                resultado = form['result'].value()
                p = Paciente(data=data,tipo=tipo,nome=nome,resultado=resultado)
                p.save()
                return HttpResponseRedirect(reverse('pacientes:results'))

        return render(request, 'index.html', {'form': form})
