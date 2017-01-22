from .models import Message
from django.http import HttpResponse


def read_message(request):
    message = Message.objects.get(id=request.POST['message_id'])
    message.readed = True
    message.save()
    return HttpResponse('OK')
