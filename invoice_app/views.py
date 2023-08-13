from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import InvoiceForm
from .forms import InvoiceForm
from .models import InvoiceModel
from django.core.files.base import ContentFile


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




def generate_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pdf_data = generate_pdf(data)
            response = HttpResponse(pdf_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

            if pdf_data:
                invoice = InvoiceModel(
                    order_date=data['order_date'],
                    invoice_id=data['invoice_id'],
                    client_name=data['client_name'],
                    number = data['number'],
                    email = data['email'],
                    address=data['address'],
                    database_name=data['database_name'],
                    data_filter_details = data['data_filter_details'],
                    database_price = data['database_price'],
                    total_price = data['total_price'],
                    payment_via = data['payment_via'],
                    agent_name = data['agent_name'],
                )
                

                pdf_file = ContentFile(pdf_data)
                pdf_file.name = 'invoice.pdf'
                invoice.pdf = pdf_file

                return response
            

                # Save the PDF file in the Invoice instance
                # pdf_file = ContentFile(pdf_data)
                # pdf_file.name = 'invoice.pdf'
                # invoice.pdf.save(pdf_file.name, pdf_file)
                # response = generate_pdf(invoice)
                # if response:
                #     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
                #     return response
        # return redirect('success') 
    else:
        form = InvoiceForm()
    return render(request, 'invoice_app/generate_invoice.html', {'form': form})


# import io
# from django.shortcuts import render, redirect
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.conf import settings
# from django.core.files.base import ContentFile
# from .forms import InvoiceForm
# from .models import InvoiceModel

# def generate_invoice(request):
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST, request.FILES)
#         if form.is_valid():

#             invoice = InvoiceModel(
#                 order_date=form.cleaned_data['order_date'],
#                 invoice_id=form.cleaned_data['invoice_id'],
#                 client_name=form.cleaned_data['client_name'],
#                 number=form.cleaned_data['number'],
#                 email=form.cleaned_data['email'],
#                 address=form.cleaned_data['address'],
#                 database_name=form.cleaned_data['database_name'],
#                 data_filter_details=form.cleaned_data['data_filter_details'],
#                 database_quantity=form.cleaned_data['database_quantity'],
#                 database_price=form.cleaned_data['database_price'],
#                 total_price=form.cleaned_data['total_price'],
#                 payment_via=', '.join(form.cleaned_data['payment_via']),
#                 agent_name=form.cleaned_data['agent_name']
#             )
#             invoice.save()
#             # # Generate PDF
#             # template_path = 'invoice_app/invoice_template.html'
#             # context = {'invoice': invoice}
#             # template = get_template(template_path)
#             # html = template.render(context)
#             # pdf_file = io.BytesIO()
#             # pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), pdf_file)
            
#             # # Save PDF to the model
#             # invoice = form.save(commit=False)
#             # pdf_content = pdf_file.getvalue()
#             # invoice.invoice_pdf.save(f'invoice_{invoice.id}.pdf', ContentFile(pdf_content))
#             # response = pdf_content(invoice)
#             # if response:
#             #     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
#             #     return response
#             return redirect('success', invoice_id=invoice.id)
#     else:
#         form = InvoiceForm()
#     return render(request, 'invoice_app/generate_invoice.html', {'form': form})



# def success_view(request):
#     return render(request, 'invoice_app/success.html')
