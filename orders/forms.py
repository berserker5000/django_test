from django import forms


class CheckOut_contact_form(forms.Form):
    name = forms.CharField(required=True)
    phone= forms.CharField(required=True)