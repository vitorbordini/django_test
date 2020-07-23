from django.urls import path

from . import views

app_name = 'pacientes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('adicionar/', views.AddView.as_view(), name='adicionar'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('excluir/', views.ExcluirView.as_view(), name='excluir'),
    path('results/', views.add, name='add'),
    #path('exc/', views.excluir, name='excluir'),
]

