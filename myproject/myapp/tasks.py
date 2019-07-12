
from myproject.celery import app
import paho.mqtt.client as mqtt
import json


MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "qubercomm"


# Define on_publish event function
def on_publish(client, userdata, mid):
    print("#########Message Published###############3...")


def on_connect(client, userdata, flags, rc):
    print("##############-on_connect########################")
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)


def on_message(client, userdata, msg):
    print("###########-on_message################-")
    print(msg.topic)
    #print(msg.payload)
    payload = json.loads(msg.payload)  # convert string to json
    print(payload)
    #client.disconnect()  # Got message then disconnect






@app.task(name="mytask")
def publish(payload):
    print("publish payload")
    global MQTT_MSG
    MQTT_MSG = json.dumps(payload);
    # Initiate MQTT Client
    mqttc = mqtt.Client()

    # Register publish callback function
    mqttc.on_publish = on_publish
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    mqttc.loop_forever();

