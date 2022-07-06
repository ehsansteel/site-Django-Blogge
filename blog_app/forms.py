from django import forms






class ContactUsForms(forms.Form):
    input = forms.CharField(max_length=12, label="type is form")
