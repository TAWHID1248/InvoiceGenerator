from django import forms


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


# from django import forms
# from .models import InvoiceModel

# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = InvoiceModel
#         fields = '__all__'  # Use all fields from the model
#         widgets = {
#             'order_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'invoice_id': forms.TextInput(attrs={'class': 'form-control'}),
#             'client_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'number': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'youremail@domain.com'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'database_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'data_filter_details': forms.TextInput(attrs={'class': 'form-control'}),
#             'database_quantity': forms.TextInput(attrs={'class': 'form-control'}),
#             'database_price': forms.TextInput(attrs={'class': 'form-control'}),
#             'total_price': forms.TextInput(attrs={'class': 'form-control'}),
#             'payment_via': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
#             'agent_name': forms.TextInput(attrs={'class': 'form-control'}),
#         }
