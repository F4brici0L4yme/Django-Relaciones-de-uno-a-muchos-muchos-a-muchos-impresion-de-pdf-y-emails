from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

def generar_boleta_pdf(request):
    # Simulación de datos (puedes cambiarlos por modelos reales)
    cliente = {
        'nombre': 'Yarbis',
        'correo': 'yarbis@email.com',
    }

    productos = [
        {'nombre': 'Laptop', 'precio': 2500.00},
        {'nombre': 'Mouse Gamer', 'precio': 150.00},
        {'nombre': 'Teclado Mecánico', 'precio': 300.00},
    ]

    total = sum(p['precio'] for p in productos)

    template = get_template('boletas/boleta.html')
    html = template.render({
        'cliente': cliente,
        'productos': productos,
        'total': total,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'

    pisa_status = pisa.CreatePDF(
        io.BytesIO(html.encode('utf-8')), dest=response, encoding='utf-8'
    )

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response
