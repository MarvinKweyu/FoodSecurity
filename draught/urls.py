from django.urls import path, include

from . import views

urlpatterns = [
    # /app1
    path("", views.IndexView.as_view(), name="index"),
    path("plot1d/$", views.Plot1DView.as_view(), name="plot1d"),
]
