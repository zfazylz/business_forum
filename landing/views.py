from django.shortcuts import render
from django.views import generic
from .forms import FeedBackForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class ContactFormView(generic.FormView):
    template_name = 'landing/contact_form.html'
    form_class = FeedBackForm

    # success_url = '/'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, _('form submission success'))
        return reverse_lazy('feedback')

    # def form_valid(self, form):
    #     form.save()
    #     messages.success(self.request, "Your password is changed")
    #     return render(self.request, self.template_name, self.get_context_data())
