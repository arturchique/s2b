from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path("hello/", HelloView.as_view()),
    # path("six_animals/", TopSixAnimalsView.as_view()),
    # path("animal/<str:animal_id>/", AnimalView.as_view()),
    # path("filtered_animals/", AnimalFilterView.as_view()),
    # path("applications/<str:user_id>", ClientsApplicationsView.as_view()),
    # path("quiz/", ClientsApplicationsView.as_view())
    path("admin/", AdminView.as_view()),
    path("admin/add/", AdminAddView.as_view()),
    path("admin/report/", AdminReport.as_view())
]