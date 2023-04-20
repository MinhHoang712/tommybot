from django.shortcuts import render

# Create your views here.
# views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pymessenger import Bot
import json
from .models import *
from tommy.facebook_config import FB_PAGE_TOKEN
from django.views import generic
from pprint import pprint
from .chatgpt_response import *
# Khởi tạo đối tượng Bot với Page Token
bot = Bot(FB_PAGE_TOKEN)
def send_message(recipient_id, message_text):
    # response = generateText(message_text)
    
    # bot.send_text_message(recipient_id=recipient_id, message=response)
    
    bot.send_text_message(recipient_id=recipient_id, message=message_text)
    
    
class tommybot(generic.View):
    def get(self, request, *arg, **kwagrs):
        if self.request.GET['hub.verify_token'] =='123456':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    # pprint(message)
                    recipient_id = message['sender']['id']
                    message_text = message['message']['text']
                    pprint(message_text)
                    pprint(recipient_id)
                    send_message(recipient_id=recipient_id, message_text=message_text)
        return HttpResponse()