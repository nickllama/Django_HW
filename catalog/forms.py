from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    phone = forms.CharField(label='Your Phone', max_length=100)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
