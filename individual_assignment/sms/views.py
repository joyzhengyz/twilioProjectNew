from django.shortcuts import render
from twilio.rest import TwilioRestClient
from .forms import SMS

# Create your views here.
def sms(request):
    if request.method == 'POST':
        form = SMS(request.POST)
        if form.is_valid():

            number = form.cleaned_data['to']
            message = form.cleaned_data['message']
            msg_body = 'Hello form Firstname Lastname "' + message + '"'

            ACCOUNT_SID = "AC133500ef845c78de23e4b408362b99d4"
            AUTH_TOKEN = "c1210639f308905ecbc4ddd2c534945e"
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

            client.messages.create( to = number, from_ = "+17472310123", body = msg_body,)
            result = 'Done!!! "' + message + '" to ' + str(number)

            return render(request, 'sms.html', {'form': form, 'result': result})

    else:
        form = SMS()
        result = " "
    return render(request, 'sms.html', {'form': form, 'result': result})