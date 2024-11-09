import paho.mqtt.client as mqtt
import json
from .models import cheepNecklace


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to mqtt")
        client.subscribe("data/sensors")
    else:
        print(f"connection to mqtt failed")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        print(f"recieved json: {data}")

        cheepNecklace.objects.create(
            idNecklace=data["idMouton"],
            acceleration=data["acc"],
            gyroscope=data["gyr"],
            pulse=data["pulse"],
            temperature=data["temp"],
            time=data["time"]
        )
    except json.JSONDecodeError as e:
        print(f"JSON failed {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()
