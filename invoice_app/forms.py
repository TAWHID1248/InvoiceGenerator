from django import forms

# class InvoiceForm(forms.Form):
#     order_date = forms.DateField()
#     client_name = forms.CharField(max_length=100)
#     number = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea)
#     database_name = forms.CharField(max_length=100)
#     data_filter_details = forms.CharField(widget=forms.Textarea)
#     database_quantity = forms.IntegerField(min_value=1)
#     database_price = forms.DecimalField(max_digits=10, decimal_places=2)
#     total_price = forms.DecimalField(max_digits=10, decimal_places=2)
#     payment_via = forms.MultipleChoiceField(choices=[
#         ('credit_card', 'Credit Card'),
#         ('paypal', 'PayPal'),
#         ('bank_transfer', 'Bank Transfer'),
#         ('cash', 'Cash'),
#     ], widget=forms.CheckboxSelectMultiple)
#     agent_name = forms.CharField(max_length=100)

from django import forms

class InvoiceForm(forms.Form):
    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class':'form-control'}))
    invoice_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    client_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'youremail@domain.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    database_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    data_filter_details = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    database_quantity = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    database_price = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    total_price = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    payment_via = forms.MultipleChoiceField(
        choices=[
            ('crypto_currency', 'Crypto Currency'),
            ('UPI', 'UPI'),
            ('bank_transfer', 'Bank Transfer'),
            ('payoneer', 'Payoneer'),
            ('wise', 'Wise')
            ],
        widget=forms.CheckboxSelectMultiple(attrs={"class":"form-control", 'class':'form-check-label', 'class':'form-check', })
    )
    agent_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

