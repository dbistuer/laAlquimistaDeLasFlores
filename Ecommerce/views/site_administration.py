from django.shortcuts import render, redirect

from Ecommerce.paths import get_path
from Ecommerce.paths.site import Site_Path
from Ecommerce.paths.types import Type_Path


def error(request):
    return render(request, get_path(Type_Path.SITE, Site_Path.ERROR))