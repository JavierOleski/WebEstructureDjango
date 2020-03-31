from django.shortcuts import render
from .forms import Form_ficha_basica
from .models import Ficha_basica


def crear_ficha_basica(request):
    form = Form_ficha_basica(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "ficha.html", context)

def detalle_ficha_basica(request):
        obj = Ficha_basica.objects.get(id=1)
        context = {
            'object': obj
        }
        return render(request, "detalle.html", context)
