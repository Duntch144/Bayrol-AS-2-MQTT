import paho.mqtt.client as mqtt
import time

# Callback function when connecting to the source broker
def on_connect_source(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the source broker with result code " + str(rc))
        client.subscribe("d02/Id Bayrol Equipment/#")
    else:
        print(f"Failed to connect to the source broker with result code {rc}")

# Callback function when a message is received from the source broker
def on_message(client, userdata, msg):
    print("Message received: " + msg.topic + " " + str(msg.payload))
    forward_message(msg)

# Callback function when connecting to the destination broker
def on_connect_destination(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the destination broker")
    else:
        print(f"Failed to connect to the destination broker with result code {rc}")

# Callback function for disconnecting from the destination broker
def on_disconnect_destination(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection from the destination broker with result code {rc}")
    else:
        print("Disconnected from the destination broker")

# Forward the message to the destination broker
def forward_message(msg):
    forward_client.publish("Bayrol/" + msg.topic, msg.payload)
    print("Message sent: " + "Bayrol/" + msg.topic + " " + str(msg.payload))

# Initialize the destination MQTT client
forward_client = mqtt.Client()
forward_client.username_pw_set("Local Broker login", "Local Broker password")
forward_client.on_connect = on_connect_destination
forward_client.on_disconnect = on_disconnect_destination

# Connect to the destination broker
forward_client.connect("Local Broker IP", 1883, 60)
forward_client.loop_start()

# Initialize the source MQTT client with WebSockets
source_client = mqtt.Client(transport='websockets')
source_client.username_pw_set("Bayrol Websockets site login", "pass1")

source_client.tls_set()  # Use the system's default CA certificates
source_client.on_connect = on_connect_source
source_client.on_message = on_message

# Connect to the source MQTT broker via WebSockets
source_client.connect("www.bayrol-poolaccess.de", 8083, 60)
source_client.loop_forever()

# Stop the loop and disconnect properly when the script is interrupted
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    source_client.loop_stop()
    source_client.disconnect()
    forward_client.loop_stop()
    forward_client.disconnect()
