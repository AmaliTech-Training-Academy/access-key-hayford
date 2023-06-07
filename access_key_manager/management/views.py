from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import AccessKeyForm
import datetime as dt
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from .models import *


# Create your views here.
class ListView(ListView):
    model = Key
    template_name = 'management/key_detail.html'
    ordering = ['name']

def revoke_key(request, pk):
    access_key_by_id = get_object_or_404(Key, id=pk)
    access_key_by_id.status = 'revoked'
    access_key_by_id.save()
    messages.success(request,'Access-key has been revoked successfully')
    return redirect('adminapp:access_key_list')

def generate_key(request, pk):
    form = AccessKeyForm()
    user = request.user
    user_by_id = School.objects.get(id=pk)
    if request.method == 'POST':
        form = AccessKeyForm(request.POST)
        if form.is_valid():
            access_key =form.save(commit=False)
            access_key.key = form.generate_access_key()
            access_key.school = user_by_id
            if access_key.expiry_date and access_key.expiry_date < dt.date.today():
                messages.warning(request, 'Expiry date cannot be in the past')
                return redirect('management:generate', user_by_id.id)
            else:
                access_key.expiry_date = form.cleaned_data['expiry_date']
            access_key.save()

            email_body = render_to_string('school/purchase_key_mail.html', {
                    'user': user,
                    'schools': user_by_id,
                    'domain': get_current_site(request).domain,
                    'access_key': Key.objects.filter(School).first()
                })
            email_body = strip_tags(email_body)
            email_subject = 'Access Key Granted'
            email = send_mail(email_subject, email_body,from_email=user.email, recipient_list=[settings.EMAIL_HOST_USER])
            # email.send()
            return redirect('management: access_key_list', user_by_id.id)
        else:
            form = AccessKeyForm()
    return render(request, 'management/access_key_generate.html',{'form':form, 'schools': user_by_id})


def update_key(request, pk):
    access_key = get_object_or_404(Key, id=pk)
    if request.method == 'POST':
        form = AccessKeyForm(request.POST, instance= access_key)
        if form.is_valid():
            if access_key.expiry_date and access_key.expiry_date < dt.date.today():
                messages.warning(request, 'Expiry date cannot be in the past')
                return redirect('management:access_key_update', access_key.id)
            else:
                access_key.expiry_date = form.cleaned_data['expiry_date']
            access_key.save()
            messages.success(request,'Access-key has been Updated')
            return redirect('management:access_key_list')
    else:
        form = AccessKeyForm(instance= access_key)
    return render(request, 'management/access_key_update.html',{'form':form, 'access_key': access_key})