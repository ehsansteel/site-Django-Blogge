from django import forms
from django.core.validators import ValidationError
from post_app.models import Message_form_user


class ContactUsForms(forms.Form):
    BIRTH_YEAR_CHOICES = ['1380', '1381', '1382', '1383', '1384', '1385', '1386', '1387', '1388', '1389', '1390']
    name = forms.CharField(max_length=12, label="type is name")
    username = forms.CharField(max_length=12, label="type is username")
    BIRTH_YEAR = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "form-control"}))
    Email = forms.EmailField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)

    # non_error
    def clean(self):
        name = self.cleaned_data.get("name")
        username = self.cleaned_data.get("username")

        if name == username:
            raise ValidationError("username and name are same", code="name.username")
        # else:
        #     if name != username:
        #         raise ValidationError("username and name are same", code="name.username")



# form is model data damin *

class MassageForm(forms.ModelForm):
    class Meta:
        model = Message_form_user
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'type is name'
            }),
            "Text": forms.Textarea(attrs={
                "class": 'form-control',
                "placeholder": 'Comment'
            }),
            "Email": forms.EmailInput(attrs={
                "class": 'form-control',
                "placeholder": 'type is email'
            }),
        }



# fields = ('name', 'title', 'Email', 'Password')

# fields

# exclude

# required = False forms box No tepy
