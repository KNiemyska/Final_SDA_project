from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ContactForm, UserUpdateForm, ProfileUpdateForm
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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST, instance=request.user) #instance add to have already field information
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} Your account has been updated !')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user) #instance add to have already field information
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={'u_form':u_form,
             'p_form':p_form}
    return render(request,'users/profile.html',context)


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