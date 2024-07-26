from django.shortcuts import render

from .models import User

def rols_required(*rols):
    """
    Decorador que verifica que el usuario tenga los roles requeridos. Para usarlo, se debe pasar una lista de roles
    como el siguiente ejemplo:
    @rols_required('servicios_adicionales', ['personal_direccion', 'cliente']) -> servicios_adicionales AND (personal_direccion OR cliente)
    @param rols: lista de roles requeridos ('visitante', 'cliente', 'gestor_solicitudes', 'servicios_adicionales', 'organizador_eventos', 'personal_direccion')
    """
    def decorator(func):
        def inner(request, *args, **kwargs):
            if request.user.is_authenticated:
                is_valid = True

        return inner

    return decorator