from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response

def generar_pdf(request):
    context = {
        'titulo': 'Reporte de Prueba',
        'items': ['Uno', 'Dos', 'Tres', 'Cuatro']
    }
    return render_to_pdf('reporte.html', context)
