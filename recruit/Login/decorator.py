from django.http import HttpResponse
from django.shortcuts import redirect


def usuario_no_autenticado(ver_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base')
        else:
            return ver_func(request, *args, **kwargs)
    return wrapper_func


def vistas_autorizadas(allowed_roles=[]):
    def decorador(ver_func):
        def wrapper_func(request, *args, **kwargs):
            grupo = None
            print(allowed_roles)
            if request.user.groups.exists():
                grupo = request.user.groups.all()[0].name
            for rol in grupo:
                if grupo in allowed_roles:
                    return ver_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Usted no está autorizado a ver esta página')
        return wrapper_func
    return decorador
