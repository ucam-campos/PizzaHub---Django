from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cadastro', views.Cadastar, name='cd'),
    url(r'^mostrar', views.MostarValores, name='mts'),
	url(r'^apagar', views.Apagar, name='apg'),
]
