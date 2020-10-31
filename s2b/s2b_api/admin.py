from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import *


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', )


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefecture', )