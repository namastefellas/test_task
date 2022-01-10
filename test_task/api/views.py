import json
from django.http import HttpResponse
from webapp.models import Card


def success_activate(request, *args, **kwargs):
        if request.body:
            body = request.body
            parce_json = json.loads(body)
            card = Card.objects.get(id=int(parce_json['id']))
            card.card_status = True
            card.save()
            return HttpResponse('Ok!')
        else:
            return HttpResponse('Incorrect format.')


def reject_activate(request, *args, **kwargs):
        if request.body:
            body = request.body
            parce_json = json.loads(body)
            card = Card.objects.get(id=int(parce_json['id']))
            card.card_status = False
            card.delete = True
            card.save()
            return HttpResponse('Denied')
        else:
            return HttpResponse('Incorrect format.')