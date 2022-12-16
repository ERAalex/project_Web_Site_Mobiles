from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def email_check(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['email'], 'erapyth@gmail.com',
                             ['moonanamiss@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Сообщение успешно отправлено')
                return redirect('index')
            else:
                messages.error(request, 'Письмо не отправлено')
        else:
            messages.error(request, 'Письмо не отправлено')
    else:
        form = ContactForm()
    return form