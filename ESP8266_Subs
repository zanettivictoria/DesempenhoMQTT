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
    t = msg.decode('utf-8')  # convertendo a mensagem em byte para string
    if topic == b'Led':
        if t== '1':
            print('Digitou 1')
            c.publish(topic='Resposta', msg=b'1')
            led1.value(1)
        elif t=='0':
            print("Digitou 0")
            led1.value(0)
            c.publish(topic='Resposta', msg=b'0')
        else:
            print('ops')

c = MQTTClient("Ledzinhos", '172.16.106.81',  port=1883)
c.connect()
c.set_callback(msg_callback)
c.subscribe('Led')
print('Conectei')
while True:
    c.wait_msg()
    
