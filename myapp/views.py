from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render, redirect
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils.translation import gettext as _
from .models import UserProfile, Notification,Notification2,Notification3

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required
import smtplib

import logging
from django.contrib import messages
logger = logging.getLogger('admin_logger')


from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages

def qr_code_view(request):
    # Generate the QR code
    data = "http://127.0.0.1:8000/"  # Replace with your desired data for the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Create a byte stream to save the image
    image_stream = BytesIO()
    qr_img.save(image_stream, "PNG")
    image_stream.seek(0)

    # Create an HTTP response with the image
    response = HttpResponse(content_type="image/png")
    response.write(image_stream.getvalue())

    return response



@login_required
def service1(request):
    
    if request.method == 'POST':
        notification = Notification.objects.create(
            user = request.user,
            message = request.POST.get("message")     
        )
        notification.save()
        messages.success(request, 'The form has been submitted successfully.')
        #return redirect('success')
        return render(request, 'success.html')
    return render(request, 'service1.html')

    
@login_required
def service2(request):
    
    if request.method == 'POST':
        notification = Notification2.objects.create(
            user = request.user,
            message = request.POST.get("message")     
        )
        notification.save()
        messages.success(request, 'The form has been submitted successfully.')
        #return redirect('success')
        return render(request, 'success.html')
    return render(request, 'service2.html')


@login_required
def service3(request):
    
    if request.method == 'POST':
        notification = Notification3.objects.create(
            user = request.user,
            message = request.POST.get("message")     
        )
        notification.save()
        messages.success(request, 'The form has been submitted successfully.')
        #return redirect('success')
        return render(request, 'success.html')
    return render(request, 'service3.html')



def success(request):
    return render(request,'success.html')

def home(request):
    return render(request, 'home.html')


def bin1(request):
    return render(request, 'bin1.html')

def bin2(request):
    return render(request, 'bin2.html')

def bin3(request):
    return render(request, 'bin3.html')

def bin4(request):
    return render(request, 'bin4.html')





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            message = form.cleaned_data.get('message')
            UserProfile.objects.create(
                user=user,
                email=email,
                password=password,
                message=message
            )
            # Automatically log the user in after registration
        return redirect('services')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def service4(request):
    return render(request,'service4.html')




def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('services')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})






def services(request):
    return render(request, 'services.html')


#def service1(request):
#    return render(request, 'service1.html')


def submission_list(request):
    submissions = UserProfile.objects.message()
    return render(request, 'submission_list.html', {'submissions': submissions})



def logout(request):
    auth_logout(request)
    return redirect('home')

def language_view(request):
    if request.method == 'POST':
        language_code = request.POST['language']
        request.session['django_language'] = language_code
        return redirect('home')
    else:
        return render(request, 'language.html')
    


def admin(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        users = User.objects.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))
    else:
        users = User.objects.all()

    context = {
        'users': users,
        'search_query': search_query if request.method == 'POST' else '',
    }
    return render(request, 'user_list.html', context)


def language_selection(request):
    return render(request, 'language_selection.html')



