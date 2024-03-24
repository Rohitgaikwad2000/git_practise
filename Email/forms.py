
from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='To')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
