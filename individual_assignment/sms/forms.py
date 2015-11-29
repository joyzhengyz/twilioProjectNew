from django import forms
 
class SMS(forms.Form):
    to = forms.IntegerField()
    message = forms.CharField(max_length=160)