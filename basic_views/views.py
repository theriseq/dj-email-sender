from django.shortcuts import render
from sender import core as sender


def home_view(request):
    context = {}
    if request.method == 'POST':
        emails = request.POST['recipients-inp']
        subject = request.POST['subject-inp']
        msg = request.POST['content-inp']

        emails = emails.split(',')
        text = ''
        for email in emails:
            text += sender.send_email(email, subject, msg)
            text += ' | '

        context['to_show'] = text
    return render(request, 'basic_views/home.html', context)

