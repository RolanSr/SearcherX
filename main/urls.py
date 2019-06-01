from django.urls import path
from . import views
from . import attachments

urlpatterns = [
    path('main/', views.home, name="mainPage"),
    path('main/detailsearcher/', views.DetailSearcher, name="detailSearcherPage"),
    path('main/expressadds/', views.ExpressAdds, name = "expressAddsPage"),
]
