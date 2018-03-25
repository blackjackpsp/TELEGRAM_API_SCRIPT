#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print 'Got command: %s' % command
    if content_type=='text':
      print "Messaggio ricevuto"
      bot.sendMessage(chat_id, "Ciao ciccio come stai?")
    #if command == 'on':
    #   bot.sendMessage(chat_id, on(11))
    #elif command =='off':
    #   bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('483217473:AAFYD5hwjPO6Q4hrLcmv1Evmxw6DSyfeMBg')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
