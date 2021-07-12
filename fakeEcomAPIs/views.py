from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from rest_framework_api_key.models import APIKey
#
#
# def sendmail(request):
#     ctx = {
#         'email': "borse.aman@rediffmail.com",
#         'api': "qwertyuiopasdfghjklzxcvbn"
#            }
#     message = get_template('email.html').render(ctx)
#     msg = EmailMessage('API key for dummy E-com data', message, 'borseaman16@gmail.com', ['borseaman16@gmail.com'],
#                        )
#     msg.content_subtype = "html"  # Main content is now text/html
#     msg.send()
#     print("Mail successfully sent")
