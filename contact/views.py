from django.shortcuts import render, redirect
from .models import Info
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.

def send_messages(request):
    myinfo = Info.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        email_msg = EmailMessage(
            subject=f"New Message: {subject} (From: {name})",
            body=(
                f"--- Contact Form Details ---\n"
                f"Name: {name}\n"
                f"Email: {user_email}\n"
                f"Topic: {subject}\n"
                f"---------------------------\n\n"
                f"Message Body:\n{message}"
            ), 
            from_email=settings.EMAIL_HOST_USER,             
            to=[settings.EMAIL_HOST_USER], 
            reply_to=[user_email],  
        )
        try:
            email_msg.send()
            messages.success(request, "Your message has been sent successfully!")
            # return redirect('contact')
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")
        
        
    context = {'myinfo':myinfo}
    return render(request, 'contact/contact.html',context)