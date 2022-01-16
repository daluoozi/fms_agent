import paho.mqtt.client as mqtt
import threading
import sys
import signal

def quit(signum, frame):
    print("stop")
    sys.exit()

class MqttClient:
    def __init__(self):
        ip = "39.103.227.255"
        port = 1883
        user = "mosquitto"
        pwd = "mosquitto"
        self.client = mqtt.Client()
        self.client.username_pw_set(user, pwd)
        self.client.connect(ip, port,120)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message


    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def subscribe(self, topic):
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        self.client.subscribe(topic)
        self.client.loop_forever(retry_first_connection=True)
