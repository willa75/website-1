from django import forms


class SlackInviteForm(forms.Form):
    """Form for slack invitation requests"""
    email = forms.EmailField(label='Email')
