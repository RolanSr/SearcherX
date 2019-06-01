from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="mainPage"),
    path('detailsearcher/', views.DetailSearcher, name="detailSearcherPage"),
    path('expressadds', views.ExpressAdds, name = "expressAddsPage"),
]
