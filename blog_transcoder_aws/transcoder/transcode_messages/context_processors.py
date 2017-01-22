from .models import Message


def message_context_processor(request):
    if request.user.is_anonymous():
        return {'messages': []}
    return {'messages': Message.objects.filter(readed=False)}
