from django.urls import path, include

from . import views

# UKDe2LFEt3eicgQ

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("plot1d/", views.Plot1DView.as_view(), name="plot1d"),
    path("pasture-quality/", views.KenyanMap.as_view(), name="kenyan_map"),
]
