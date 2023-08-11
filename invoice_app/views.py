from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import InvoiceForm

def generate_pdf(data):
    template_path = 'invoice_app/invoice_template.html'
    context = {'data': data}
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


# def success_view(request):
#     return render(request, 'invoice_app/success.html')

def generate_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = generate_pdf(data)
            if response:
                response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
                return response
        # return redirect('success') 
    else:
        form = InvoiceForm()
    return render(request, 'invoice_app/generate_invoice.html', {'form': form})





def success_view(request):
    return render(request, 'success.html')
