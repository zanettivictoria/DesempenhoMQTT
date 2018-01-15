import platform
import paho.mqtt.client as mqtt     # MQTT
import binascii
import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P8_10",GPIO.OUT)

def on_connect(client, userdata, flags, rc):  #Função que faz a conexão e se inscreve no tópico
    print('conectado')
    client.subscribe("Resposta")
def on_message(client, userdata, msg):  #Função que lê, publica e faz ação com o que é lido
    msga=str(msg.payload)
    topic = str(msg.topic)
    if topic == 'Resposta':
        if msga == '1':
            GPIO.output("P8_10", GPIO.HIGH)
            print('Mensagem Enviada_1')
        elif msga == '0':
            GPIO.output("P8_10", GPIO.LOW)
            print('Mensagem Enviada_0')
        else:
            pass

if __name__ == '__main__':   #Verifica o sistema operaconal o qual este código está rodando, para que seja feita a conexão correta
    is_windows = platform.system() == 'Windows'
    is_linux = platform.system() == 'Linux'
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.subscribe("Resposta")
    client.loop_start()

    if is_linux:
        client.connect("172.16.106.81", 1883, 60)  #Broker
    else:
        client.connect("172.16.106.81", 1883, 60)
   #Mensagem que é publicada
    for i in range (0,1000):
        print('Vou mandar')
        msgs = '1'
        client.publish(topic='Led', payload=msgs)
        time.sleep(0.2)
        client.publish(topic='Led', payload='0')
        time.sleep(0.2)



