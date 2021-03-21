from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from ritmista_app.views import (CursosViewset, GruposViewset, NaipesViewset,
                                RitmistasViewset, ListaRitmistasNaipe, exporta_csv)
from ritmista_app import views

# rota principal
router = routers.DefaultRouter()

router.register('cursos', CursosViewset, basename='Cursos')
router.register('grupos', GruposViewset, basename='Grupos')
router.register('naipes', NaipesViewset, basename='Naipes')
router.register('ritmistas', RitmistasViewset, basename='Ritmistas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('naipe/<int:pk>/ritmistas/', ListaRitmistasNaipe.as_view()),
    path('csv', views.exporta_csv, name='exporta_csv')
]
