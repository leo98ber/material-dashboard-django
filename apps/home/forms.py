from django import forms

from apps.home.models import Subscription, User


class SubscriptionForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'my-custom-class'}))
    class Meta:
        """Form settings."""

        model = Subscription
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'placeholder': 'Select user'}),
            'credit_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indicate your credit card'}),
            'preferences': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Preferences'}),
            'level': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle', 'placeholder': 'Choose a subscription level'}),
        }
