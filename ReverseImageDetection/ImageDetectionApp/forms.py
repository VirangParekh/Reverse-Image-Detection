from django import forms

class UploadForm(forms.Form):
    image=forms.ImageField()
    upper_range=forms.IntegerField(min_value=0)
    lower_range=forms.IntegerField(min_value=0)

    