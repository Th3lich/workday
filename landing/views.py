from django.shortcuts import render
import threading
from django.views.generic import CreateView
from django.shortcuts import render
from django.core.mail import send_mail

from configuracion.settings import DEFAULT_FROM_EMAIL
from landing import forms


class Home(CreateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        contact_form = forms.ContactForm

        return render(request, self.template_name, {'form': contact_form})

    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)
        result = "error"
        message = "Ha habido un fallo, vuelve a intentarlo"
        recipient = 'javilpx2.jl@gmail.com'

        if form.is_valid():
            asunto = "Consulta desde Workday++: " + form['subject'].value()
            mensaje = "El usuario: " + form['email'].value() + "\n" + form['message'].value()
            t = threading.Thread(target=send_mail, args=(
                asunto, mensaje, DEFAULT_FROM_EMAIL, [recipient], False, None, None, None, mensaje))
            t.start()
            result = "success"
            message = "Mensaje enviado correctamente"


        return render(request, self.template_name, {
            'form': form
        })


class PrivacyPolicy(CreateView):
    template_name = 'privacy-policy.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})
