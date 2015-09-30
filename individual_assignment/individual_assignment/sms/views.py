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
            msg_body = 'Hello from Yezhen Zheng "' + message + '"'

            ACCOUNT_SID = "ACb1a6efea70726b9928a9dafbcf920149"
            AUTH_TOKEN = "3c8fd35ced3c74f045e4647e79b3313e"
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

            client.messages.create( to = number, from_ = "+17326866669", body = msg_body,)
            result = 'Done!!! "' + message + '" to ' + str(number)

            return render(request, 'sms.html', {'form': form, 'result': result})

    else:
        form = SMS()
        result = " "
    return render(request, 'sms.html', {'form': form, 'result': result})