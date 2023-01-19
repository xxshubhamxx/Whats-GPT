from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from twilio.rest import Client
from wa_files.openai_chat.openai_bot import ai_response
import os

load_dotenv()

sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')

app = Flask(__name__)
client = Client(sid, auth_token)



def respond(my_msg):
    response = MessagingResponse()
    response.message(my_msg)
    print(response)
    # https://developers.facebook.com/apps/889056005785574/whatsapp-business/wa-dev-console/?business_id=1375199489916704
    # from heyoo import WhatsApp
    # messenger = WhatsApp(os.getenv('WA_ACCESS_TOKEN'), phone_number_id=os.getenv('WA_PHONE_ID'))
    # messenger.send_message(str(response)[58:-21],os.getenv('MY_PHONE_NUMBER'))
    
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=my_msg,
                              to='whatsapp:+918217063115'
                          )
    print(message.sid)
    return str(response)

@app.route('/')  
def home():
    return 'Home'

@app.route('/message', methods=['GET','POST'])
def reply():
    message = request.form.get('Body').lower()
    response = ai_response(message)
    return respond(response)