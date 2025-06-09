from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Language

def frameworks_por_lenguaje(request, lenguaje_id):
    lenguaje = get_object_or_404(Language, id=lenguaje_id)
    frameworks = lenguaje.framework_set.all()
    return render(request, 'frameworks_por_lenguaje.html', {
        'lenguaje': lenguaje,
        'frameworks': frameworks
    })

