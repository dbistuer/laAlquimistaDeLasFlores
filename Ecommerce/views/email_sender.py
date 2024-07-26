
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext as _

from Ecommerce.models import User
from laAlquimistaDeLasFlores.settings.base import EMAIL_HOST_USER


def send_email(request):
    if request.method == "POST":
        recipient = request.POST.get("email", "")
        if recipient:
            user = User.objects.get(email=request.POST.get("email", ""))
            url = generate_url(request, user)
            message = get_message(user, url)
            try:
                send_mail(subject=subject,
                          message=message,
                          from_email=from_email,
                          recipient_list=[recipient],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect('done')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse("Make sure all fields are entered and valid.")

    else:
        return render(request, 'registration/password_reset_form.html')


def generate_token(user):
    prtg = PasswordResetTokenGenerator()
    return PasswordResetTokenGenerator.make_token(self=prtg, user=user)

def generate_uid(user):
    return force_str(urlsafe_base64_encode(force_bytes(user.pk)))

def generate_url(request, user):
    tkn = generate_token(user)
    uid = generate_uid(user)
    lang = request.LANGUAGE_CODE
    uri = request.build_absolute_uri()
    uris = uri.split('/')
    last = len(uris)-2
    uris[last] = 'reset'
    url = '/'.join(uris)
    url = url + uid + '/' + tkn + '/'
    return url

def get_message(user,url):
    return message_start + url + message_end + user.username + greatings

subject = "Password reset for " + "email"
message_start = "You have received this email because you have requested to reset the password for your account at " + "127.0.0.1:8000.\n" \
          "Please go to the following page and choose a new password.\n"

message_end = "Your user number, in case you have forgotten it: "
greatings = "\nThank you for using our site!\n"\
    "From the team at " + "127.0.0.1:8000"
from_email = EMAIL_HOST_USER
recipient_list = []