txt=r'''
import network
import machine
from umqtt.simple import MQTTClient
import time

led1= machine.Pin(5,machine.Pin.OUT)#Led configuração

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('NERsDUniFi', 'digi*rpi$awsom') #Conexão WIFI
print('Tentando conexão...')
while not sta_if.isconnected(): #Verificação da conexão
    pass
print('Conectado!')


def msg_callback(topic, msg):
    print('recebi')
    t = msg.decode('utf-8')  # convertendo a mensagem em byte para string
    if topic == b'Resposta':
        if t== '1':
            print('Digitou 1')
            led1.value(1)
        elif t=='0':
            print("Digitou 0")
            led1.value(0)
        else:
            print('ops')

c = MQTTClient("ESP8266", '172.16.106.81' ,  port=1883)
c.connect()
c.set_callback(msg_callback)
c.subscribe('Resposta')


print('Conectei')

while True:
    print('Vou publicar 1 e 0:')
    c.publish(topic='Led_',msg=b'1')
    c.wait_msg()


'''
f = open('main.py', 'w+')
f.write(txt)
f.close()

