from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from rest_framework_api_key.models import APIKey


#TODO add captcha in email submission.

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        validEmail = False
        try:
            validate_email(email)
            validEmail = True
        except ValidationError:
            validEmail = False
            messages.error(request,"E-mail required or Check Your e-mail.")
            return redirect("/#email")

        if sendmail(email,validEmail):
            messages.info(request, "E-mail sent successfully.")
        else:
            messages.error(request, "An error occurred. Try again later.")
        return redirect("/#email")

    else:
        return render(request,template_name='index.html')

def sendmail(email,isValid):
    if isValid:
        key = APIKey.objects.create_key(name=email)
        ctx = {
            'api': key[1]
               }
        message = get_template('email.html').render(ctx)
        msg = EmailMessage('API key for dummy E-com data', message, 'borseaman16@gmail.com', [email],
                           )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        return True
    else:
        return False


def error_page(request,exception):
    return render(request,template_name="404.html")