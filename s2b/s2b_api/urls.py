from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="S2B API",
      default_version='v1',
      description="Описание",
      terms_of_service="https://github.com/arturchique/s2b",
      contact=openapi.Contact(email="aepremyan3993@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("six_animals/", TopSixAnimalsView.as_view()),
    path("animal/<str:animal_accounting_card>/", AnimalView.as_view()),
    path("filtered_animals/", AnimalFilterView.as_view()),
    path("applications/<str:user_id>", ClientsApplicationsView.as_view()),
    path("quiz/", ClientsApplicationsView.as_view()),
    path("admin/", AdminView.as_view()),
    path("admin/add/", AdminAddView.as_view()),
    path("admin/report/", AdminReport.as_view()),
    path("admin/delete/", AdminDeleteView.as_view()),
    path("test/", TestView.as_view())
]