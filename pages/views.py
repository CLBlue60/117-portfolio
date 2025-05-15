from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body = (
                f"New message from {name}:\n"
                f"Email: {email}\n"
                f"Message: {message}"
            )

            try:
                send_mail(
                    "Message from Portfolio Contact Form",
                    message_body,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                return render(request, 'pages/contact.html', {
                    'form': ContactForm(),
                    'success': True
                })

            except Exception as e:

                return render(request, 'pages/contact.html', {
                    'form': form,
                    'error': f"Failed to send message. Error: {str(e)}"
                })
        else:

            return render(request, 'pages/contact.html', {
                'form': form,
                'error': "Please correct the errors below."
            })
    else:

        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
