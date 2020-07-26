from django.http import HttpResponseRedirect

from .forms import UserRegisterForm, ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request,'users/profile.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['niemyska.katarzyna@gmail.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')