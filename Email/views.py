from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'learningperpose10@gmail.com', [to_email])
            return render(request, 'success.html')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})
