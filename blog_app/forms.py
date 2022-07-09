from django import forms
from django.core.validators import ValidationError





class ContactUsForms(forms.Form):
    name = forms.CharField(max_length=12, label="type is name")
    username = forms.CharField(max_length=12, label="type is username")

    # non_error
    def clean(self):
        name = self.cleaned_data.get("name")
        username = self.cleaned_data.get("username")
        if name == username:
            raise ValidationError("username and name are same", code="name.username")
        else:
            if name != username:
                raise ValidationError("username and name are same", code="name.username")

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if "a" in name:
            raise ValidationError("Your name is not correct", code="a_in_name")
        return name


