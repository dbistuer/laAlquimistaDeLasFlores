from django.shortcuts import render, redirect

from Ecommerce.paths import get_path
from Ecommerce.paths.site import Site_Path
from Ecommerce.paths.types import Type_Path
from django.utils.translation import gettext_lazy as _

from laAlquimistaDeLasFlores import settings


def error(request):
    return render(request, get_path(Type_Path.SITE, Site_Path.ERROR))

def set_language(request):
    lang_code = request.GET.get('language')
    response = redirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response