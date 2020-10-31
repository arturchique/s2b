from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', )


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefecture', )


@admin.register(Worker)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'shelter', )