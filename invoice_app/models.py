# from django.db import models
# from django.db import models
# from django.utils import timezone
# from django.core.files.storage import FileSystemStorage
# from reportlab.pdfgen import canvas
# from io import BytesIO

# class InvoiceModel(models.Model):
#     order_date = models.DateField()
#     invoice_id = models.CharField(max_length=100)
#     client_name = models.CharField(max_length=100)
#     number = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     database_name = models.CharField(max_length=100)
#     data_filter_details = models.CharField(max_length=200)
#     database_quantity = models.CharField(max_length=200)
#     database_price = models.CharField(max_length=200)
#     total_price = models.CharField(max_length=200)
#     PAYMENT_CHOICES = [
#         ('crypto_currency', 'Crypto Currency'),
#         ('UPI', 'UPI'),
#         ('bank_transfer', 'Bank Transfer'),
#         ('payoneer', 'Payoneer'),
#         ('wise', 'Wise'),
#     ]
#     payment_via = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
#     agent_name = models.CharField(max_length=100)
#     # invoice_pdf = models.FileField(upload_to='invoices/', blank=True, null=True)  # Store generated invoice PDF

#     invoice_file = models.FileField(upload_to='invoices/', blank=True, null=True)

#     def generate_invoice_pdf(self):
#         buffer = BytesIO()
#         p = canvas.Canvas(buffer)

#         # Your PDF generation code here
#         # Use p.drawString(), p.drawImage(), etc. to create the PDF content

#         p.showPage()
#         p.save()

#         buffer.seek(0)
#         self.invoice_file.save(f'invoice_{self.invoice_id}.pdf', buffer, save=True)
#         buffer.close()

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.generate_invoice_pdf()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.invoice_id

   

from django.db import models

class InvoiceModel(models.Model):
    order_date = models.DateField()
    invoice_id = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    database_name = models.CharField(max_length=100)
    data_filter_details = models.TextField()
    database_quantity = models.CharField(max_length=200)
    database_price = models.CharField(max_length=200)
    total_price = models.CharField(max_length=200)
    payment_via = models.CharField(max_length=200)
    agent_name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='invoices/')

    def __str__(self):
        return f"Invoice {self.invoice_id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.invoice_pdf:  # Generate PDF and store it if not already present
            from django.template.loader import get_template
            from xhtml2pdf import pisa
            from io import BytesIO

            template_path = 'invoice_app/invoice_template.html'
            context = {'data': self}
            template = get_template(template_path)
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            if not pdf.err:
                self.invoice_pdf.save(f'invoice_{self.invoice_id}.pdf', BytesIO(result.getvalue()))

            super().save(*args, **kwargs)
