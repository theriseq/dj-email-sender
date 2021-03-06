from django.core.mail import send_mail
from recipients.models import Recipient

SENDER = 'Patrick <django-email-sender@email.com>'


def send_email(recipient, subject, msg):
    recipient = recipient.replace(" ", "")
    send_mail(subject, replace_in_msg(recipient, msg), SENDER, [recipient], fail_silently=False,)

    return replace_in_msg(recipient, msg)


def replace_in_msg(recipient, msg):
    fields_to_replace = [
        'email',
        'full_name',
        'score',
    ]
    user = Recipient.objects.get(email=recipient)
    for field in fields_to_replace:
        if f'@@{field}' in msg:
            tmp_msg = msg
            user_field = f'user.{field}'
            user_field = eval(user_field)
            user_field = str(user_field)

            msg = tmp_msg.replace(f'@@{field}', user_field)

    return msg
