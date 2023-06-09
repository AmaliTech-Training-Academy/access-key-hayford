# import from rest_framework library
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import AccessKeyForm, MailForm, SchoolForm
import datetime as dt
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.contrib.auth.models import User


# Create your views here.
class ListView(ListView):
    model = Key
    template_name = 'management/key_detail.html'
    ordering = ['user']

def revoke_key(request, pk):
    access_key_by_id = get_object_or_404(Key, id=pk)
    access_key_by_id.status = 'revoked'
    access_key_by_id.save()
    messages.success(request,'Access-key has been revoked successfully')
    return redirect('management:key_list')
    # return render(request, 'management/key_list.html')

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
            if access_key.expiry_date and access_key.expiry_date.date() < dt.date.today():
                messages.warning(request, 'Expiry date cannot be in the past')
                return redirect('management:update_key', access_key.pk)
            else:
                access_key.expiry_date = form.cleaned_data['expiry_date']
            access_key.save()
            messages.success(request,'Access-key has been Updated')
            return redirect('management:key_list')
    else:
        form = AccessKeyForm(instance= access_key)
    return render(request, 'management/api_update_form.html', {'form':form, 'access_key': access_key})


class AccessKeyViewAPI(APIView):
    def get(self, request):
        form = MailForm(request.GET)
        if request.method == 'GET':
            email = request.cleaned_data['email']
            school = School.objects.get()
            key = Key.objects.get(status=Key.status['active'])
            return Response(serializers.data)
        return render(request, '/management/api-form.html')
    




#School Dashboard 
def school_dashboard(request):
    form = SchoolForm()
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            school = School.objects.create(name=name,  user=user)
            school.save()
            return redirect('management:access_key_list',  id=school.id)
        else:
            form = SchoolForm()
    return render(request,'school/school_view.html', {'form':form})


def key_request(request, pk):
    school = School.objects.get(id=pk)
    context = {'school':school}
    return render(request,'school/key_request.html', context)


def School_key_view(request, pk):
    user = request.user
    school = get_object_or_404(School, id=pk)
    key = Key.objects.filter(school=school)
    return render('school/dashboard.html', {'school':school, 'key':key, 'user':user})