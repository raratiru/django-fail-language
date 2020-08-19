from django import forms
from letsagree.models import Term
from django.utils.translation import get_language


class PendingConsentForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = (
            "summary_{0}".format(get_language()),
        )
