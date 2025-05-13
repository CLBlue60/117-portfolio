from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("The Data is valid")

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
                    "Email from Portfolio",
                    message_body,
                    email,
                    ['blueofill@gmail.com'],

                )
                print("Email sent successfully")

                return render(request, 'pages/contact.html', {'form': form})


            except Exception as e:
                print(f"Error sending the email: {e}")
                return render(request, 'pages/contact.html', {
                     'form': form,
                     'error': str(e)
                })

        else:
                print("The Data is not valid")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
