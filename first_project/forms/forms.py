from django import forms
from django.core import validators

## example of personalized validator
"""
def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError('NAME NEEDS TO START WITH Z')
"""


class FormName(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    verify_email = forms.EmailField(label='Enter your email again', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}),
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError('Email must match')


## replaced with the validator attribute
'''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("NO BOTS ALLOWED :)")
        return botcatcher
'''
