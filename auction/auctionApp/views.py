from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Question

def index(request):
    return HttpResponse("Auction App.")

def postQuestion(request, item_id, asker_id):
    if request.method == "POST":
        postData = json.loads(requests.body.decode("utf-8"))

        _asker = User.objects.get(id = asker_id)
        _item = Item.objects.get(id = item_id)
        _question = postData.get('question')

        Question.objects.create(question = _question, asker = _asker, item = _item)
        response = JsonResponse({'status' : 'question posted'})

        return response
    return HttpResponseBadRequest('Invalid request')

def getQuestions(request, item_id, asker_id):
    if request.method == "GET":
        _item = Item.objects.get(id = item_id)
        _asker = User.objects.get(id = asker_id)

        questionData = Question.objects.values('question', 'answer')

        data = {
            'answer' : list()
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def postAnswer(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id = question_id)

        postData = json.loads(request.body.decode("utf-8"))

        _answer = postData.get('answer')

        question.newAnswer(_answer)

        data = {
            'updated' : True
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')


def postItem(request, seller_id):
    if request.method == "POST":
        postData = json.loads(request.body.decode("utf-8"))

        _name = postData.get('name')
        _desc = postData.get('description')
        _start_time = postData.get('startTime')
        _end_time = postData.get('endTime')
        _start_price = postData.get('startPrice')
        _cur_price = postData.get('currentPrice')
        _image = postData.get('image')
        _seller = postData.get('seller')

        Item.objects.create(name = _name, desc = _desc,
            start_time = _start_time, end_time = _end_time,
            cur_price = _cur_price, image = _image, seller = _seller)

        data = {
            'status' : 'user added'
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def getItem(request, item_id):
    if request.method == "POST":
        item = Item.objects.get(id = item_id)

        itemData = item.values('name', 'desc', 'start_time', 'end_time',
         'start_price', 'cur_price', 'image', 'seller')

         data = {
            'item' : itemData
         }

         return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def placeBid(request, item_id):
    if request.method == "POST":
        item = Item.objects.get(id = item_id)

        postData = json.loads(request.body.decode("utf-8"))

        _bid = postData.get('bid')

        data = {}

        if _bid > item.cur_price:
            item.newBid(_bid)
            data = {
                'status' : 'bid placed'
            }
        else:
            data = {
                'status' : 'ivalid bid'
            }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')
