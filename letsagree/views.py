from django.views.generic import FormView
from letsagree.forms import TestView


class PendingView(FormView):
    form_class = TestView
