import Adafruit_BBIO.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setup("P8_10",GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    client.subscribe("Led")

def on_message(client, userdata, msg):
    t =str(msg.payload)
    topic=str(msg.topic)
    if topic == 'Led':
        print(t)
        if t == '1':

            GPIO.output("P8_10", GPIO.HIGH)
            client.publish(topic='Resposta', payload='1')
            print('liguei')
        elif t == '0':

            GPIO.output("P8_10", GPIO.LOW)
            client.publish(topic='Resposta', payload= '0')
            print('desliguei')
        else:
            pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.16.106.81", 1883, 60)
print('passei')
client.subscribe("Led")
client.loop_forever()

