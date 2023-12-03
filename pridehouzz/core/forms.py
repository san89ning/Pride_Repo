from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    email_address = forms.EmailField(widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
