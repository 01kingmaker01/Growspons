
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import  get_template


def sendMail(request, email, mailFor, msg, subject):
    content = {'mailFor':mailFor}

    if msg == 'AddPAndWelcome':
        template = get_template('authentication/email.html').render(content)

    elif msg== 'acceptDeal':
        template = get_template('authentication/acceptemail.html').render(content)    

    else:
        pass
    
    if not subject:
        subject = 'Welcome to The Growspons'

    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        email,
    )

    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()